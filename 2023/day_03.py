from collections import defaultdict
import math

data = list(map((lambda x : "."+x+"."), open("input/day3.txt").read().splitlines()))
data = ["." * len(data[0])] + data + ["."* len(data[0])]

def do_assingment(n):
    gears, r = defaultdict(list), 0

    for y in range(len(data)):
        number, nc = "", []
        for x in range(len(data[y])):
            if data[y][x].isnumeric():
                number += data[y][x]
                nc.append(complex(x,y))
            elif not data[y][x].isnumeric() and number:
                nc = [nc[0] + -1] + nc + [nc[-1] + 1]
                nc += [c + -1j for c in nc] + [c + 1j for c in nc]
                for c in nc:
                    point = data[int(c.imag)][int(c.real)]
                    if point == "*" and n:
                        gears[c].append(int(number))
                    elif not point.isnumeric() and not point == "." and not n:
                        r += int(number)
                        break
                number, nc = "", []
    return sum([math.prod(x) for x in gears.values() if len(x) == 2]) if n else r

print(do_assingment(0))
print(do_assingment(1))
