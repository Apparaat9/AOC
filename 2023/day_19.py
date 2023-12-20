from collections import defaultdict
import math

def get_intersect(ranges):
    return min(x[-1] for x in ranges) - max([x[0] for x in ranges]) + 1

def revert_rules(rules):
    result, v = [], None
    for k, v in rules.items():
        sp, rp, mp = ('<', '>', -1) if '<' in k else ('>', '<', 1)
        t,d = k.split(sp)
        r = f"{t}{rp}{int(d)+mp}"
        result.append(r)
    return result, v

def make_ranges(rules):
    results = defaultdict(list)
    for k in rules:
        if '<' in k:
            t, d = k.split('<')
            results[t].append((1,int(d)-1))
        else:
            t, d = k.split('>')
            results[t].append((int(d)+1,4000))
    return results

def get_rules(rules):
    nr = {}
    for rule in rules.split():
        name, seq = rule.split("{")
        seq = [x.split(':') for x in seq[:-1].split(',')]
        seq[-1] = ['True', seq[-1][0]]
        nr[name] = {s : a for s,a in seq}
    return nr

def do_assignment_two(rules):
    to_do = [['in']]
    done = []
    while to_do:
        current = to_do.pop()
        current_method = current.pop()
        seen = {}
        for k, v in rules[current_method].items():
            new_current = current.copy()
            ek, _ = revert_rules(seen)
            seen[k] = v
            new_current += ek + [k, v] if k != 'True' else ek + [v]

            if v not in 'AR':
                to_do.append(new_current)
            elif v in 'A':
                done.append(new_current)

    total = 0
    for d in done:
        rules = make_ranges(d[:-1])
        sub_total = [get_intersect(v) for v in rules.values()]
        sub_total += [4000] * (4 - len(rules))
        total += math.prod(sub_total)
    print(total)

rules, parts = open('input/day19.txt').read().split('\n\n')
rules = get_rules(rules)

res = 0
x, m, a, s = 0, 0, 0, 0
for idx, part in enumerate(parts.split()):
    current = 'in'
    for o in part[1:-1].split(','):
        exec(o)
    while current not in 'AR':
        for k, v in rules[current].items():
            if eval(k):
                current = v
                break
    if v == 'A':
        res += x + m + a + s
print(res)

do_assignment_two(rules)


