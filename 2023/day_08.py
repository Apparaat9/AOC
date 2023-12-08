import math
directions, _, *nodes = open('input/day8.txt').read().splitlines()
node_map = {a.split()[0] : {"L" : a.split()[2][1:-1], "R" : a.split()[3][:-1]} for a in nodes}

def do_assigment(n):
    currents = [x for x in node_map if x[-1] == 'A'] if n else ['AAA']
    z_steps = [0] * len(currents)
    steps = 0

    while not all(z_steps):
        for direction in directions:
            steps += 1
            currents = [node_map[c][direction] for c in currents]
            z_steps = [steps if c[-1] == 'Z' and not z_steps[idx] else z_steps[idx] for idx, c in enumerate(currents)]

    return math.lcm(*z_steps)

print(do_assigment(0))
print(do_assigment(1))