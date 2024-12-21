import re

M = {complex(i, t) : y for i, x in enumerate(open('input/day_20.txt').read().splitlines()) for t, y in enumerate(x)}

def pmap(s):
    for x in range(max(int(i.real) for i in M) + 1):
        for y in range(max(int(i.imag) for i in M) + 1):
            coord = complex(x, y)
            print(M[coord] if coord not in s else 'X', end='')
        print('')

start, end = [k for k in M if M[k] in 'SE']

def get_path():
    c, s = start, [start]
    while M[c] != 'E':
        for d in [1, -1, 1j, -1j]:
            if M[c + d] != '#' and c+d not in s:
                c = c + d
                s.append(c)
    return s

def get_cheats():
    data = open('input/day_20.txt').read().splitlines()
    ud = [*map(''.join, map(list, zip(*data)))]

    cheats = []
    for i, x in enumerate(data):
        for m in re.finditer(r'(?=(\.|E|S)#(S|\.|E))', x):
            cheat_start = m.span()[0]
            cheat_finish = cheat_start + 2
            cheats.append((complex(i, cheat_start), complex(i, cheat_finish)))

    for i, x in enumerate(ud):
        for m in  re.finditer(r'(?=(\.|E|S)#(S|\.|E))', x):
            cheat_start = m.span()[0]
            cheat_finish = cheat_start + 2
            cheats.append((complex(cheat_start, i), complex(cheat_finish, i)))

    return cheats

def get_in_range(point):
    s = set()
    for x in range(int(point.real) - 20, int(point.real) + 21):
        for y in range(int(point.imag) - 20, int(point.imag) + 21):
            s.add(complex(x,y))
    return s

path = get_path()
tries = []
saving = 100
for i, p in enumerate(path):
    candidates = path[min(i + saving, len(path) - 1):]
    candidates = get_in_range(p) & set(candidates)
    print(len(path), i, len(candidates), len(tries))
    for c in candidates:
        md = abs(p.real - c.real) + abs(p.imag - c.imag)
        if (path.index(c) - i) - md >= saving and md <= 20:
            tries.append((path.index(c) - i) - md)

print(len(tries))
