pipes = {"|" : {"N","S"}, "-" : {"E","W"}, "L" : {"N","E"}, "J" : {"N","W"},"7" : {"S","W"}, "F" : {"S","E"}, "S" : {"N", "W", "E", "S"}}
trans = {"N" : "S", "S" : "N", "E" : "W", "W" : "E"}
ctrans = {"N" : -1, "S" : 1, "E" : 1j, "W" : -1j}

data = open("input/day10.txt").read().splitlines()
pipe_map = {complex(y,x) : data[y][x] for x in range(len(data[0])) for y in range(len(data))}

start = {x for x in pipe_map if pipe_map[x] == 'S'}.pop()
next = {k for k, v in ctrans.items() if trans[k] in pipes[pipe_map[start + v]]}.pop()

current = start + ctrans[next]
route = [start]

while current != start:
    route.append(current)
    next = (pipes[pipe_map[current]] - set(trans[next])).pop()
    current += ctrans[next]

print(int(len(route) / 2))

## Lazy but it's sunday, I'll come back to write my own implementation
import matplotlib.path as mpltPath

polygon = [[x.real, x.imag] for x in route]
path = mpltPath.Path(polygon)
a = [1 for k in pipe_map if k not in route and path.contains_points([[k.real, k.imag]])]

print(len(a))
