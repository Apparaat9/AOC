from collections import defaultdict

T = [1, 1j, -1, -1j]
M = {complex(i, t) : y for i, x in enumerate(open('input/day_12.txt').read().split()) for t, y in enumerate(x)}
                      
def get_group(c, k, s):
    r = set()
    if c not in M or c in s or M[c] != k:
        return set()
    if M[c] == k:
        r.add(c)
    
    s.add(c)
    for d in T:
        r |= get_group(c + d, k, s) 
    return r

F = defaultdict(list)
for k in M:
    if any(k in x['set'] for x in F[M[k]]):
        continue
    F[M[k]] += [{'set' : get_group(k, M[k], set()), 'corners' : 0}]

for plots in F.values():
    for plot in plots:
        for p in plot['set']:
            cc = [(-1j,-1),(-1,1j),(1j,1),(1,-1j)]
            plot['corners'] += sum(all(x+p not in plot['set'] for x in n) for n in cc)

        plot['perim'] = [x+i for i in T for x in plot['set'] if x+i not in plot['set']]
        for p in set(plot['perim']):
            cc = [(-1j,-1, -1-1j),(-1,1j,-1+1j),(1j,1, 1j+1),(1,-1j, 1-1j)]
            plot['corners'] += sum(all(x+p in plot['set'] for x in n) for n in cc)


r1 = sum(len(plot['set']) * len(set(plot['perim'])) for plots in F.values() for plot in plots)
r2 = sum(len(plot['set']) * plot['corners'] for plots in F.values() for plot in plots)
print(r1, r2)