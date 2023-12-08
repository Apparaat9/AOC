import copy
import itertools
import re


def get_numbers(string):
    return [int(x) for x in re.findall(r'\d+',string)]

def get_between_coords(c1, c2):
    result = []
    target = 1 if c1[0] == c2[0] else 0
    minimal = min(c1[target], c2[target])
    for i in range(abs(c1[target] - c2[target]) + 1):
        if target:
            result.append([c1[0], minimal + i])
        else:
            result.append([minimal + i, c1[1]])
    return result


def build_the_wall(game_input):
    rock_coords = []
    for coords in game_input:
        for i in range(len(coords) - 1):
            rock_coords += get_between_coords(coords[i], coords[i+1])

    x_s = sorted([x[0] for x in rock_coords])
    y_s = sorted([x[1] for x in rock_coords])

    wall = [['.' for x in range(x_s[-1] - x_s[0] + 1)] for x in range(y_s[-1] + 1)]
    for rock in rock_coords:
        wall[rock[1]][rock[0]-x_s[0]] = '#'
    wall[0][500 - x_s[0]] = '+'
    return wall

def print_wall(wall):
    print('\n'.join([''.join(x) for x in wall]))


def move_down(x, y):
    if wall[y + 1][x] != '.':
        if wall[y + 1][x - 1] != '.':
            if wall[y + 1][x + 1] != '.':
                return x, y
            else:
                return move_down(x + 1, y + 1)
        else:
            return move_down(x - 1, y + 1)
    else:
        return move_down(x, y+1)

def assigment_one(wall):
    start = wall[0].index('+')
    for i in itertools.count():
        try:
            x, y = move_down(start, 0)
            wall[y][x] = 'o'
        except IndexError:
            break
    print_wall(wall)
    print(f"Units: {i}")

def assignment_two(wall):
    for i in range(len(wall)):
        padding = ['.' for _ in range(len(wall))]
        wall[i] = padding + wall[i] + padding

    wall.append(['.' for _ in range(len(wall[0]))])
    wall.append(['#' for _ in range(len(wall[0]))])

    start = wall[0].index('+')

    for i in itertools.count():
        x, y = move_down(start, 0)
        if (x,y) == (start, 0):
            print_wall(wall)
            break
        wall[y][x] = 'o'
    print(f"Units: {i + 1}")

game_input = [list(map(get_numbers,x.split(' -> '))) for x in open("input/day14_input.txt", "r").read().splitlines()]

wall = build_the_wall(game_input)
assigment_one(wall)

wall = build_the_wall(game_input)
assignment_two(wall)