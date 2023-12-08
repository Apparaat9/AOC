import re
import sys


def get_numbers(string):
    return [int(x) for x in re.findall(r'\d+|-\d+',string)]

def manhatten_difference(x):
    return abs(x.real) + abs(x.imag)


def parse_sensors(game_input):
    sensors = []
    occupied = set()

    for coords in game_input:
        s = complex(coords[0], coords[1])
        b = complex(coords[2], coords[3])
        reach = int(manhatten_difference(s-b))
        occupied.add(s), occupied.add(b)
        sensors.append([s, reach])
    return sensors, occupied


def assignment_1(sensors, occupied):
    print(f"Time for a stretch")
    x_coords = sorted([int(x[0].real) for x in sensors])
    min_x, max_x = x_coords[0], x_coords[-1]
    max_reach = max([x[1] for x in sensors])

    score = 0
    for i in range(min_x - max_reach, max_x + max_reach, 1):
        point = complex(i,2000000)
        for s in sensors:
            if point not in occupied and manhatten_difference(s[0] - point) <= s[1]:
                score += 1
                break
    print(f"Answer: {score}\n")

def assignment_2(sensors):
    print(f"You should go get some coffee")
    limit = 4_000_001
    i = 0
    while i < limit:
        if i % 100000 == 0: print(f"Checked:\t{i}")
        y = 0
        while y < limit:
            point = complex(i, y)
            scores = [s[1] - abs(manhatten_difference(s[0] - point)) for s in sensors]
            if not any([x >= 0 for x in scores]):
                print(f"Score: {point.real * 4_000_000 + point.imag}")
                exit()
            else:
                y += max(scores) + 1
        i += 1

game_input = map(get_numbers, open("input/day15_input.txt", 'r').read().splitlines())
sensors, occupied = parse_sensors(game_input)

assignment_1(sensors, occupied)
assignment_2(sensors)