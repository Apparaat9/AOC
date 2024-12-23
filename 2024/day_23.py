from collections import defaultdict
from itertools import combinations, permutations

pcs = defaultdict(set)
for link in open('input/day_23.txt'):
    conn = set(link.strip().split('-'))
    for x in conn:
        pcs[x] |= conn - {x}

print(sum(all(a in pcs[b] for a, b in permutations(trio, 2)) for trio in combinations(pcs.keys(), 3) if any(y.startswith('t') for y in trio)))

clique = defaultdict(set)
for k, conns in pcs.items():
    for x in conns:
        clique[k] |= conns & pcs[x] | {k}

print(*sorted(max(clique.values(), key=lambda x : list(clique.values()).count(x))), sep=',')