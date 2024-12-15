def get_group(c, d, s):
    if M[c] in '[]@O' and c not in s:
        s.add(c)
        if M[c] == '[':
            s |= get_group(c + step['>'], d, s)
        elif M[c] == ']':
            s |= get_group(c + step['<'], d, s)
        s |= get_group(c + d, d, s)
        return s if all(s) else set()
    elif M[c] == '#':
        return {0}
    else:
        return set()

def look_ahead(c, d):
    if M[c] != '.':
        look_ahead(c+d, d)
        cs = M[c]
        M[c] = M[c+d]
        M[c+d] = cs

def do_run(m):
    global M
    M = {complex(i, t) : y for i, x in enumerate(m.split()) for t, y in enumerate(x)}
    current = [k for k, v in M.items() if v == '@'][0]

    for d in D.replace('\n',''):
        boxes = get_group(current, step[d], set())
        for move in boxes - set(x+step[d] for x in boxes):
            look_ahead(move, step[d])    
        current += step[d] if boxes else 0

    print(sum(100*k.real + k.imag for k, v in M.items() if v in '[O'))

m, D = open('input/day_15.txt').read().split('\n\n')
step = {'^' : -1, '>' : 1j, '<' : -1j, 'v' : 1}

do_run(m)
do_run(m.replace('#', '##').replace('O','[]').replace('.','..').replace('@','@.'))