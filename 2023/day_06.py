import math
from sympy import symbols, solve

data = open('input/day6.txt').read().splitlines()

def do_assignment(n, fancy=False):
    time, distance = [[int(''.join(t.split()[1:]))] if n else [int(x) for x in t.split()[1:]] for t in data]
    scores = []

    if fancy:
        for rt, rd in  zip(time, distance):
            x = symbols('x')
            min, max = solve(((int(rt) - x) * x) - int(rd))
            scores.append(int(max) - int(min))
    else:
        for idx, time in enumerate(time):
            race = [(time - i) * i for i in range(1,time)]
            scores.append(len([x for x in race if x > distance[idx]]))

    return math.prod(scores)


print(do_assignment(0))
print(do_assignment(1))

print(do_assignment(0, fancy=True))
print(do_assignment(1, fancy=True))