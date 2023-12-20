data = open("input/day16.txt").read().splitlines()
width, height = len(data[0]), len(data)
table_map = {complex(y,x) : data[y][x] for x in range(width) for y in range(height)}

dir_map = {1 : {'.' : [1], '\\' : [1j], '/' : [-1j], "|" : [1], "-" : [1j, -1j]},
           -1: {'.' : [-1], '\\' : [-1j], '/' : [1j], "|" : [-1], "-" : [1j, -1j]},
           1j: {'.' : [1j], '\\' : [1], '/' : [-1], "|" : [1, -1], "-" : [1j]},
           -1j: {'.' : [-1j], '\\' : [-1], '/' : [1], "|" : [1, -1], "-" : [-1j]}}


def check_point(start, dir):
    to_do = [[x,(start)] for x in dir_map[dir][table_map[start]]]
    seen = set()

    while to_do:
        dir, cur = to_do.pop()
        seen.add((dir, cur))
        next_point = cur + dir
        if next_point in table_map:
            for next_dir in dir_map[dir][table_map[next_point]]:
                if (next_dir, next_point) not in seen:
                    to_do.append([next_dir, next_point])
    return (len(set([x[1] for x in seen])))

results = []
for i in range(width):
    results.append(check_point(complex(0, i), 1))
    results.append(check_point(complex(height-1, i), -1))

for i in range(height):
    results.append(check_point(complex(i, 0), 1j))
    results.append(check_point(complex(i, width-1), -1j))

print(max(results))