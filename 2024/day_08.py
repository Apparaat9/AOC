from collections import defaultdict
from itertools import permutations

G = defaultdict(set)

for i, x in enumerate(open('input/day_08.txt')):
    for t, y in enumerate(x.strip()):
        G[y].add(complex(i, t))

all = G.pop('.') | {y for x in G.values() for y in x}

def do_run(q):
    an = set()
    for coords in G.values():
        for a, b in permutations(coords, 2):
            an |= set(a+n*(a-b) for n in range(*q))
    return len(all.intersection(an))

print(do_run((1,2)))
print(do_run((0 ,50)))