ts = []
for i, n in enumerate(open('input/day_09.txt').read()):
    if n != '0':
        ts.append((int(n), str(i//2) if i % 2 == 0 else '.'))


def solve1(ts):
    r1 = [y for x, n in ts for y in x*[n]]
    while '.' in r1:
        if (x := r1.pop()) != '.':
            r1[r1.index('.')] = x
    print(sum(i * int(id) for i, id in enumerate(r1)))

def solve2(ts):
    for c in ts[::-1]:
        if c[1] == '.':
            continue
        for r_i, r in enumerate(ts[:ts.index(c)]):
            if r[1] == '.' and r[0] >= c[0]:
                if not r[0] - c[0]:
                    del ts[r_i]
                else:
                    ts[r_i] = [r[0] - c[0], '.']
                ts[ts.index(c)] = [c[0], '.']
                ts.insert(r_i, c)
                break            

    r1 = [y for x, n in ts for y in x*[n]]
    print(sum(i * int(id) if id != '.' else 0 for i, id in enumerate(r1)))

solve1(ts)
solve2(ts)