
data = open('input/day_25.txt').read().split('\n\n')
things = [{(i, t) for t, y in enumerate(k) for i, x in enumerate(y.split()) if x == '#'} for k in data]
print(sum(not (t & x) for t in things for x in things )//2)