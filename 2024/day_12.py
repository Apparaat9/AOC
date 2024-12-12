from collections import defaultdict
M = {complex(i, t) : y for i, x in enumerate(open('input/day_12.txt').read().split()) for t, y in enumerate(x)}

def pmap(M ,s=set()):
    for i, x in enumerate(open('input/day_12.txt').read().splitlines()):
        for t, _ in enumerate(x):
            point = complex(i, t)
            print(M[point] if point not in s else '.', end='')
        print('')
                      
def get_group(c, k, s):
    this_result = set()
    if c not in M or c in s or M[c] != k:
        return set()
    if M[c] == k:
        this_result.add(c)
    
    s.add(c)
    for d in [1, -1, 1j, -1j]:
        this_result |= get_group(c + d, k, s) 
    return this_result

F = defaultdict(list)
for k in M:
    if any(k in x['set'] for x in F[M[k]]):
        continue
    F[M[k]] += [{'set' : get_group(k, M[k], set()), 'perim' : [], 'corners' : 0}]


r1 = 0

for key in F.values():
    for s in key:
        s['perim'] = {x+i for i in [1, -1, 1j, -1j] for x in s['set']} - s['set']
        r1 += len(s['set'])*len(s['perim'])

for letter, plots in F.items():
    for plot in plots:
        for p in plot['set']:
            nn = [d not in plot['set'] for d in [p + t for t in [1, -1, 1j, -1j]]].count(True)
            if nn:
                for pt in [(-1j,-1),(-1,1j),(1j,1),(1,-1j)]:
                    if all(d not in plot['set'] for d in [p + t for t in pt]):
                        plot['corners'] += 1

        for p in set(plot['perim']):
            nn = [d in plot['set'] for d in [p + t for t in [1, -1, 1j, -1j]]].count(True)
            if nn:
                for pt in [(-1j,-1, -1-1j),(-1,1j,-1+1j),(1j,1, 1j+1),(1,-1j, 1-1j)]:
                    if all(d in plot['set'] for d in [p + t for t in pt]):
                        plot['corners'] += 1

r2 = 0
for letter, plots in F.items():
    for plot in plots:
        r2 += len(plot['set']) * plot['corners']
print(r1, r2)