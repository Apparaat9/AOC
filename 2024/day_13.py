from sympy import solve, Integer
from sympy.abc import x, y
import re

prizes = [[*map(int, re.findall('\d+', x))] for x  in open('input/day_13.txt').read().split('\n\n')]

def gobroke(offset=0):
    R = 0
    for x1, y1, x2, y2, xa, ya in prizes:
        s = solve([x*x1+y*x2-(offset + xa),x*y1+y*y2-(offset +ya)])
        if all(isinstance(s[n], Integer) for n in s):
            R += 3*s[x] + s[y]
    return R

print(gobroke())
print(gobroke(10000000000000))

