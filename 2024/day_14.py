import re
from collections import Counter
from functools import reduce

def do_step(c, d):
    return (c.real + d.real) % H + (c.imag + d.imag) % W * 1j

W, H = 101, 103

data = [[*map(int, re.findall(r'-*\d+', x))] for x in open('input/day_14.txt').read().splitlines()]
robots = [(complex(cc, cr), complex(dc,dr)) for cr, cc, dr, dc in data]

for i in range(10_000):  
    robots = [(do_step(*r), r[1]) for r in robots]
    current = [v[0] for v in robots]
    if len(current) == len(set(current)):
        print(i+1)
        break
    if i == 99:
        qv = Counter([(x.real <  H//2, x.imag < W//2) for x in current if x.real != H//2 and x.imag != W//2])
        print(reduce(lambda x, y: x*y, qv.values()))
