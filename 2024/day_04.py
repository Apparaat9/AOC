data = open('input/day_04.txt').read().splitlines()

lr = data
ud = [*map(''.join, map(list, zip(*data)))]

crossud, crosslr = [], []
start = 0
for i in range(len(data[0])):
    ncu = ncd = ncl = ncr = ''
    for j in range(len(data) - i):
        ncu += data[i][j]
        ncd += data[j][i]
        ncl += data[::-1][i][j]
        ncr += data[::-1][j][i]
        i += 1
    crossud += [ncu] + [ncd]
    crosslr += [ncl] + [ncr]

print(sum(x.count('XMAS') + x.count('SAMX') for x in lr + ud + crossud[1:] + crosslr[1:]))

coords = [[0,0], [0,2], [1,1], [2,0], [2,2]]
check = ['MMASS', 'MSAMS', 'SSAMM', 'SMASM']
r = []
for x in range(len(data[0]) - 2):
    for y in range(len(data) - 2):
        r += [''.join([data[c[0] + x][c[1] + y] for c in coords])]

print(len([x for x in r if x in check]))