from collections import defaultdict
from itertools import combinations, permutations

pcs = defaultdict(set)
for link in open('input/day_23.txt'):
    conn = set(link.strip().split('-'))
    for x in conn:
        pcs[x] |= conn - {x}

print(sum(all(a in pcs[b] for a, b in permutations(trio, 2))for trio in filter(lambda x : any(y.startswith('t') for y in x), combinations(pcs.keys(), 3))))

clique = defaultdict(set)
for k, conns in pcs.items():
    connectivity = set()
    for x in conns:
        connectivity |= conns & pcs[x]
    clique[k] = connectivity | {k}

print(*sorted(max(clique.values(), key=lambda x : list(clique.values()).count(x))), sep=',')