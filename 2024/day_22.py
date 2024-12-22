from collections import defaultdict

def evolve(n):
    m = n ^ n * 64 % 16777216
    q = m ^ m // 32 % 16777216
    r = q ^ q * 2048 % 16777216
    return r

data = [*map(int, open('input/day_22.txt').read().splitlines())]
f = defaultdict(lambda : 0)
r1 = 0

for i, d in enumerate(data):
    seq, seen = tuple(), set()
    price = d % 10

    for _ in range(2000):
        d = evolve(d)
        seq += (d % 10 - price,)
        price = d % 10

        if len(seq) < 4:
            continue

        if seq not in seen:
            f[seq] += price
            seen.add(seq)

        seq = tuple(list(seq)[1:])
    r1 += d

print(r1, max(x for x in f.values()))