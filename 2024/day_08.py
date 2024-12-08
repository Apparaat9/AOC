from collections import defaultdict
from itertools import permutations


data = {complex(i, t):y for i, x in enumerate(open('input/day_08.txt').read().split()) for t, y in enumerate(x)}

G = defaultdict(list)
all = set(data.keys())

for coord, s in data.items():
    G[s] += [coord]

G.pop('.')

def do_run(q):
    an = set()
    for coords in G.values():
        for a, b in permutations(coords, 2):
            if q: an.add(a)
            adiff = (a-b)
            while(a in all):
                a = a+adiff
                an.add(a)
                if not q: break
    return len(all.intersection(an))

print(do_run(0))
print(do_run(1))