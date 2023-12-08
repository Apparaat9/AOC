import copy
import re

import networkx as nx


def get_data(string):
    return re.findall('[A-Z]{2}|\d+', string)

def fill_graph(game_input):
    g = nx.Graph()

    for data in game_input:
        g.add_node(data[0], rate=int(data[1]), set=False)
        for n in data[2:]:
            g.add_edges_from([(data[0], n)])

    return g

game_input = list(map(get_data, open('input/day16_input.txt','r').read().splitlines()))
graph = fill_graph(game_input)
sps = {x[0]: x[1] for x in nx.all_pairs_shortest_path_length(graph)}

class SearchTree():

    shortest_paths = sps

    def __init__(self, g, sps):
        self.value = 0
        self.tick = 30
        self.current = 'AA'
        self.g = g
        self.activated = []
        self.shortest_paths = sps
        self.potens = self.get_potential_values()

    def get_options(self):
        return [x for x in self.g.nodes if x not in self.activated and x != self.current and self.g.nodes[x]['rate'] != 0]

    def get_shortest_path(self, s, t):
        return self.shortest_paths[s][t]

    def get_potential_values(self):
        return {k : (self.tick - (self.get_shortest_path(self.current, k) + 1)) * self.g.nodes[k]['rate'] for k in self.get_options() if (self.tick - (self.get_shortest_path(self.current, k) + 1)) >= 1}

    def get_stats(self):
        return print(f"Current: {self.current}\tTick: {self.tick}\tValue: {self.value}\tActivated: {self.activated}")

    def go_to(self, n):
        clone = copy.deepcopy(self)
        clone.tick -= self.get_shortest_path(self.current, n) + 1
        clone.current = n
        clone.g.nodes[n]['set'] = True
        clone.potens = self.get_potential_values()
        clone.value += clone.potens[n]
        clone.activated.append(n)
        return clone


def do_assigment_one(g):
    trees = [SearchTree(g, sps)]
    final_trees = []

    while trees:
        new_trees = []
        for tree in trees:
            options = tree.get_potential_values()
            for option in options:
                new_trees.append(tree.go_to(option))
            else:
                final_trees.append(tree)
        trees = new_trees

    for tree in sorted(final_trees, key= lambda x: x.value):
        tree.get_stats()


class DoubleSearchTree:

    shortest_paths = sps

    def __init__(self, g):
        self.value = [0,0]
        self.tick = [26,26]
        self.current = ['AA','AA']
        self.g = g
        self.activated = []

    def get_options(self, number):
        return [x for x in self.g.nodes if x not in [y[1] for y in self.activated] and x != self.current[number] and self.g.nodes[x]['rate'] != 0]

    def get_shortest_path(self, s, t):
        return self.shortest_paths[s][t]

    def get_potential_values(self, number):
        return {k : (self.tick[number] - (self.get_shortest_path(self.current[number], k) + 1)) * self.g.nodes[k]['rate'] for k in self.get_options(number) if (self.tick[number] - (self.get_shortest_path(self.current[number], k) + 1)) >= 0}

    def get_potential_gain(self, i, target):
        options = self.get_options(i)
        values = []
        for k in options:
            if k != target:
                time_left = (self.tick[i] - ((self.get_shortest_path(self.current[i], target)) + (self.get_shortest_path(target, k) + 1)))
                if time_left > 0:
                    potent = time_left * self.g.nodes[k]['rate']
                    values.append(potent)
                else:
                    values.append(0)
        return sum(values)

    def get_stats(self):
        return print(f"Current: {self.current}\tTick: {self.tick}\tValues: {self.value}\tValue: {sum(self.value)}\tActivated: {self.activated}")

    def go_to(self, nodes):
        clone = copy.deepcopy(self)
        for number in range(len(nodes)):
            clone.tick[number] -= self.get_shortest_path(self.current[number], nodes[number]) + 1
            clone.value[number] += self.get_potential_values(number)[nodes[number]]
            clone.current[number] = nodes[number]
            clone.g.nodes[nodes[number]]['set'] = True
            clone.activated.append([number, nodes[number]])
        return clone


def do_assignment_two(g, max_value=2216):
    max_hops = len([k for k in g.nodes if g.nodes[k]['rate'] > 0])
    trees = [DoubleSearchTree(g)]
    final_trees = []
    counter = 0
    while trees:
        new_trees = []
        for tree in trees:
            options_a, options_b = tree.get_potential_values(0), tree.get_potential_values(1)

            if options_a and options_b:
                if len(options_a) == len(options_b) == 1 and list(options_a.keys()) == list(options_b.keys()):
                    for key in options_a:
                        if options_a[key] > options_b[key]:
                            new_tree = tree.go_to((key, 'AA'))
                        else:
                            new_tree = tree.go_to(('AA', key))
                    final_trees.append(new_tree)
                else:
                    pg_a, pg_b = {k: tree.get_potential_gain(0, k) + options_a[k] for k in options_a}, {
                        k: tree.get_potential_gain(1, k) + options_b[k] for k in options_b}
                    for n1 in options_a:
                        for n2 in options_b:
                            if (n1 != n2) and (sum(tree.value) + pg_a[n1] + pg_b[n2] >= max_value):
                                new_tree = tree.go_to((n1,n2))
                                if len(new_tree.activated) == max_hops:
                                    final_trees.append(new_tree)
                                else:
                                    new_trees.append(new_tree)
            else:
                final_trees.append(tree)
            counter += 1

            if counter % 1000 == 0:
                print(f"Trees done:\t{counter},\tNew Candidate Trees:\t{len(new_trees)}")

        if new_trees:
            max_value = max(max_value, max([sum(x.value) for x in new_trees]))
            trees = new_trees
        else:
            trees = []

    for tree in sorted(final_trees, key= lambda x: sum(x.value))[-10:]:
        tree.get_stats()


do_assigment_one(graph)
do_assignment_two(graph)
