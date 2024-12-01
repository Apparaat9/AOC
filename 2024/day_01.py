a, b = zip(*[x.split() for x in open("input/day_01.txt").read().splitlines()])
a, b = sorted(map(int, a)), sorted(map(int, b))
r1 = [abs(a[i] - b[i]) for i in range(len(a))]
r2 = [x * b.count(x) for x in a]
print(sum(r1))
print(sum(r2))