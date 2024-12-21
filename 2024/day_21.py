from functools import cache

numpad = {'7' : (0,0), '8' : (0,1), '9' : (0,2),
          '4' : (1,0), '5' : (1,1), '6' : (1,2),
          '1' : (2,0), '2' : (2,1), '3' : (2,2),
                       '0' : (3,1), 'A' : (3,2)}

d_pad = {            '^' : (0,1), 'A' : (0,2),
        '<' : (1,0), 'v' : (1,1), '>' : (1,2)}

checks = {'<' : (0,-1), '>' : (0,1), '^' : (-1,0), 'v' : (1,0)}

def get_pushes(current, target, pad):
    p = d_pad if pad else numpad
    hd, vd = map(lambda x : x[0]-x[1], zip(p[current], p[target]))
    ha = abs(hd) * ('v' if hd < 0 else '^')
    va = abs(vd) * ('<' if vd > 0 else '>')
    r = ha + va
    
    seen = [p[current]]
    for t in r: 
        seen.append([*map(lambda x : x[0]+x[1], zip(seen[-1], checks[t]))])
    sk = '>^v<' if (pad and [0,0] in seen) or (not pad and [3,0] in seen) else '<v^>'
    pushes = ''.join(sorted(r, key=lambda x : sk.index(x)))

    return pushes

@cache
def push(seq, max_depth, depth=0, pad=0):
    if depth == max_depth:
        return len(seq) if pad else seq
    r = 0 if pad else ''

    current = 'A'
    for i in range(len(seq)):
        r += push(get_pushes(current, seq[i], pad) + 'A', max_depth, depth+1, pad)
        current = seq[i]
    return r

data = open('input/day_21.txt').read().splitlines()
for q in 2, 25:
    print(sum(push(push(d, 1), q, pad=1) * int(d.removesuffix('A')) for d in data))

    
