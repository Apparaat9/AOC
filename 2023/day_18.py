from itertools import groupby
from operator import itemgetter
from collections import defaultdict

def is_inside_sm(polygon, point):
    length = len(polygon) - 1
    dy2 = point[1] - polygon[0][1]
    intersections = 0
    ii = 0
    jj = 1

    while ii < length:
        dy = dy2
        dy2 = point[1] - polygon[jj][1]

        if dy * dy2 <= 0.0 and (point[0] >= polygon[ii][0] or point[0] >= polygon[jj][0]):
            if dy < 0 or dy2 < 0:
                F = dy * (polygon[jj][0] - polygon[ii][0]) / (dy - dy2) + polygon[ii][0]
                if point[0] > F:
                    intersections += 1
                elif point[0] == F:
                    return 2
            elif dy2 == 0 and (point[0] == polygon[jj][0] or (
                    dy == 0 and (point[0] - polygon[ii][0]) * (point[0] - polygon[jj][0]) <= 0)):
                return 2
        ii = jj
        jj += 1
    return intersections & 1


def get_ranges(data):
    ranges = []
    for k, g in groupby(enumerate(data), lambda x:x[0]-x[1]):
        group = list(map(itemgetter(1), g))
        ranges.append((group[0], group[-1]))
    extras = []
    for i in range(len(ranges)):
        try:
            extras.append((ranges[i][-1] + 1, ranges[i+1][0] - 1))
        except:
            pass
    return extras


two = True
data = [x.split() for x in open('input/day18.txt').read().splitlines()]

route = [0 + 0j]
dir_dict = {"R" : 1j, "D" : 1, "L" : -1j, "U" : -1}
hex_dir_dict = {0 : "R", 1 : "D", 2 : "L", 3 : "U"}

y_dict = defaultdict(list)

print("Building Route")
counter = 0
polygon = [[0,0]]
for dir, count, hex in data:
    if counter % 10 == 0:
        print(f"ToDo : {len(data) - counter}")
    if two:
        count = int(hex[2:7],16)
        dir = hex_dir_dict[int(hex[-2])]
    for i in range(int(count)):
        next_point = route[-1] + dir_dict[dir]
        y_dict[int(next_point.real)].append(next_point.imag)
        route.append(route[-1] + dir_dict[dir])
    polygon.append([next_point.real, next_point.imag])
    counter += 1

route = route[:-1]

print("Checking ranges")
result = 0
total = len(list(y_dict.keys()))
counter = 0
last_sub_res = []
last_ranges = []
for k, v in y_dict.items():
    row = sorted(v)
    ranges = get_ranges(row)
    if ranges == last_ranges:
        for i in range(len(last_sub_res)):
            if last_sub_res[i]:
                result += (ranges[i][1] - ranges[i][0]) + 1
    else:
        sub_res = []
        for l, r in ranges:
            if is_inside_sm(polygon, [k,l]):
                result += (r-l) + 1
                sub_res.append(1)
            else:
                sub_res.append(0)
        last_sub_res = sub_res
        last_ranges = ranges
    counter += 1
print(result + len(route))