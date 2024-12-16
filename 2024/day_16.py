from heapq import heappush, heappop

M = {complex(i, t) : y for i, x in enumerate(open('input/day_16.txt').read().splitlines()) for t, y in enumerate(x)}
S = {k : 0  if v != '#' else -1 for k, v in M.items()}
D = {'>' : 1j, '^' : -1, 'v' : 1, '<' : -1j}
R = {'r' : set()}

def do_walk(p, c, s, d):
    c = c.pop() + D[d]
    if M[c] != '#':
        if not S[c] or S[c] >= p or (not S[c+D[d]] or S[c+D[d]] >= p):
            S[c] = p
            R['r'] |= s if M[c] == 'E' else set()
            return [(p + (1 if t == d else 1001), {c}, s | {c}, t) for t in D]
    return []


end, start = [k for k in M if M[k] in 'SE']
walks = []
heappush(walks, (0, {start - 1j}, set([start-1j]), '>'))
while walks:
    for w in (do_walk(*heappop(walks))):
        if not S[end] or w[0] < S[end]:
            heappush(walks, w)
print(S[end])
print(len(R['r']))