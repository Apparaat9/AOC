data = open('input/day2.txt','r').read().splitlines()
maxes = {"red" : 12, "green" : 13, "blue" : 14}

result = 0
sr = 0
for idx, row in enumerate(data):
    nm = {"red": 0, "green": 0, "blue": 0}

    r = row.replace(";",",").split(": ")[1].split(', ')
    w = [int(x.split()[0]) <= maxes[x.split()[1]] for x in r]
    for p in r:
        n, c = p.split()
        nm[c] = max(int(n), nm[c])
    sr += nm['red'] * nm['green'] * nm['blue']
    if all(w):
        result += (idx + 1)
print(result)
print(sr)