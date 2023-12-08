import ast
import re
from functools import reduce
from math import gcd


def get_numbers(string):
    return [int(x) for x in re.findall(r'\d+',string)]

def lmc(list):
    return reduce(lambda a,b: a*b // gcd(a,b), list)

def parse_monkeys(game_input):
    monkeys = {}
    for data in game_input:
        monkey = data.split("\n")
        monkeys[get_numbers(monkey[0])[0]] = {"items" : [int(x) for x in get_numbers(monkey[1])],
                                              "operation" : monkey[2].split("= ")[1].replace(" ",""),
                                              "test" : int(get_numbers(monkey[3])[0]),
                                              "True" : get_numbers(monkey[4])[0],
                                              "False" : get_numbers(monkey[5])[0],
                                              "count" : 0}
    return monkeys

def do_assignment(monkeys, n):
    magic = lmc([x['test'] for k,x in monkeys.items()])

    for _ in range(n):
        for monkey, values in monkeys.items():
            for old in values['items']:
                new = eval(values['operation'])
                if new > magic:
                    new = new % magic
                test = new % values['test'] == 0
                monkeys[values[str(test)]]['items'].append(new)
                values['count'] += 1
            values['items'] = []

    counted = sorted([x['count'] for k,x in monkeys.items()])
    print(counted[-1] * counted[-2])

game_input = open("input/day11_input.txt", "r").read().split("Monkey")[1:]

do_assignment(parse_monkeys(game_input), 20)
do_assignment(parse_monkeys(game_input),10000)
