from itertools import product
from functools import reduce
from operator import mul, add

data = [map(int, x.replace(':','').split(' ')) for x in open('input/day_07.txt').read().splitlines()]

com = lambda x, y: int(str(x) + str(y))
options = [mul, add, com]

r = 0
for target, *sums in data:
    for combo in map(list, product(options, repeat=len(sums)-1)):
        if target == reduce(lambda x, y: combo.pop(0)(x,y), sums):
            r += target
            break
print(r)

