from heapq import heappop, heappush

def do_walk(p, c, s):
    c = c.pop()
    if c in V and V[c] > p:
        V[c] = p
        return [(p + 1, {c + t}, s | {c}) for t in [1, -1, 1j, -1j]]
    return []

data = open('input/day_18.txt').read().splitlines()
B = [complex(*map(int, x.split(','))) for x in data]
M = {complex(x, y) for x in range(71) for y in range(71)}
start, end = complex(0,0), complex(70,70)
    
for i in range(1024, len(B)):
    V = {k : 1e9 for k in M - set(B[:i])}
    walks = [(0, {start}, set())]

    while walks: [heappush(walks, w) for w in do_walk(*heappop(walks))]

    if i == 1024:
        print(V[end])
    if V[end] == 1e9:
        print(data[i-1])
        break
