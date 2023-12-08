import copy
import math
import re
from collections import Counter

import numpy as np
from frozendict import frozendict


def should_build(robots):
    sb = {'o','c'}
    if 'c' in robots:
        sb.add('b')
    if 'b' in robots:
        sb.add('g')
    return sb


def flatten(container, types=(list,tuple)):
    for i in container:
        if isinstance(i, types):
            for j in flatten(i, types):
                yield j
        else:
            yield i


def check_resources(needed, resources):
    return all(needed[r] <= resources[r] for r in needed)


def get_new_options(blueprint, resources):
    final_options = []
    for x in ['o','c','b','g']:
        if check_resources(blueprint[x], resources):
            final_options.append(tuple(x))
    return final_options + [tuple('')]


def convert_to_frozen(d):
    if isinstance(d, dict):
        for k, v in d.items():
            d[k] = convert_to_frozen(v)
        return frozendict(d)
    return d


def get_cost_type(string):
    return re.findall('\d+\s\w+', string)


def get_numbers(string):
    return re.findall('\d+', string)


def parse_blueprints(game_input):
    blueprints = {}
    for blueprint in game_input:
        name = str(get_numbers(blueprint[0])[0])
        blueprints.update({name : {}})
        for robot_data in blueprint[1:]:
            robot_type = robot_data.split()[0][0] if robot_data.split()[0] != 'obsidian' else 'b'
            blueprints[name].update({robot_type: {}})
            cost_types = get_cost_type(robot_data)
            for cost in cost_types:
                value, material = cost.split()
                blueprints[name][robot_type].update({material[0] if material != 'obsidian' else 'b' : int(value)})
    return blueprints


def options_pruning(options, bottleneck, n=100, score=False):
    counters = [Counter(x) for x in options]
    values = [np.array([x['o'],x['c'],x['b'],x['g']]) for x in counters]
    bottleneck = Counter(bottleneck)
    bn = np.array([bottleneck['o'],bottleneck['c'],bottleneck['b'],bottleneck['g']])
    distances = [np.linalg.norm(bn - v) for v in values]
    if score:
        return distances
    options = [x for _, x in sorted(zip(distances, options))]
    return options[:n]


def distance_pruning(resource_dict, blueprint, n=10000):
    results = []
    for k, v in resource_dict.items():
        for b in v:
            distance = options_pruning(k, get_bottleneck(blueprint, k), score=True)[0]
            results.append([k, b, distance])
    results = sorted(results, key=lambda x:x[2])
    other_results = sorted(results, key=lambda x:x[1]['g'], reverse=True)
    for item in results:
        if item not in other_results[:n]:
            resource_dict[item[0]].remove(item[1])
            if not resource_dict[item[0]]:
                resource_dict.pop(item[0])
    return resource_dict


def add_to_resource_dict(resource_dict, resource, robots, black_list=False):
    if robots not in resource_dict:
        resource_dict[robots] = [resource]
        return resource_dict
    remove = []
    for r in resource_dict[robots]:
        if all([r[key] >= resource[key] for key in r]):
            if black_list:
                pass
            else:
                return resource_dict
        if not any([r[key] > resource[key] for key in r]):
            remove.append(r)

    if black_list:
        return remove
    resource_dict[robots] = [r for r in resource_dict[robots] if r not in remove] + [resource]
    return resource_dict


def add_resources(resources, robots):
    resources = dict(resources)
    for r in robots:
        resources[r] += 1
    return frozendict(resources)


def build_robot(blueprint, resources):
    resources = dict(resources)
    for k, v in blueprint.items():
        resources[k] -= v
    return frozendict(resources)


def build_robots(blueprint, resources, robots):
    for robot in robots:
        resources = build_robot(blueprint[robot], resources)
    return resources


def new_options_pruning(options, bottleneck):
    if not bottleneck:
        return [tuple([]), tuple(['g'])]
    return options

def branch_pruning(branches, robots):
    if len(set(flatten(branches)).symmetric_difference(should_build(robots))) == 0:
        if tuple() in branches:
            branches.remove(tuple())
    else:
        if tuple() not in branches:
            branches.append(tuple())
    return branches

def get_bottleneck(blueprint, robots, want='g'):
    prio = []
    got = Counter(robots)
    needed = blueprint[want]

    if want == 'o':
        return ['o'] * needed['o']

    for r in needed:
        if needed[r] > got[r]:
            prio += [r] * (needed[r] - got[r])

    for p in range(len(prio)):
        if prio[p] == 'o':
            prio += ['o'] * (needed[prio[p]] - got[p])
        else:
            prio += get_bottleneck(blueprint, robots, want=prio[p])
    return prio

def do_run(blueprint, time_limit):
    def do_turn(time, tnrd):
        if time == time_limit:
            final = []
            for robots, branches in tnrd.items():
                for final_options in branches:
                    final.append([robots, add_resources(final_options, robots)])
            return final
        nrd = {}
        for robots, branches in tnrd.items():
            bottleneck = get_bottleneck(blueprint, robots)
            for this_resource in branches:
                options = branch_pruning(get_new_options(blueprint, this_resource), robots)
                options = new_options_pruning(options, bottleneck)
                for option in options:
                    new_resources = build_robots(blueprint, copy.copy(this_resource), option)
                    new_resources = add_resources(new_resources, robots)
                    nrd = add_to_resource_dict(nrd, new_resources, tuple(sorted(robots + tuple(option))))
        nrd = distance_pruning(nrd, blueprint)
        return do_turn(time+1, nrd)

    resources = frozendict({'o': 0, 'c': 0, 'b': 0, 'g': 0})
    resource_dict = dict()
    resource_dict[tuple('o')] = [resources]
    return do_turn(1, resource_dict)


def do_assignment(blueprints, turns):
    results = []
    for k, bp in blueprints.items():
        result = do_run(bp, turns)
        result = max(result, key=lambda x: x[1]['g'])
        print(f"Did {k} for {result[1]['g']}")
        results.append((int(k), result[1]['g']))
    print(f"Quality Levels: {sum(math.prod(x) for x in results)}, Result Product: {math.prod([x[1] for x in results])}")

game_input = [x.split('Each ') for x in open("input/day19_input.txt", "r").read().splitlines()]

blueprints = convert_to_frozen(parse_blueprints(game_input))
do_assignment(blueprints, 24)

blueprints = convert_to_frozen(parse_blueprints(game_input[:3]))
do_assignment(blueprints, 32)

