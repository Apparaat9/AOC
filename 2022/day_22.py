import re
import itertools

game_input = open("input/day22_input.txt", "r").read().splitlines()
game_directions = game_input[-1]
plane = [[*x] for x in game_input[:-2]]
vertical_plane = list(map(list, itertools.zip_longest(*plane, fillvalue=" ")))

move = {"L" : 0+-1j, "R" : 0+1j, "U" : -1+0j, "D" : 1+0j}
adjust = {"R" : {"L" : "U", "R" : "D"},
          "U" : {"L" : "L", "R" : "R"},
          "L" : {"L" : "D", "R" : "U"},
          "D" : {"L" : "R", "R" : "L"}}

current_direction = "R"
game_directions = re.split("(R|L)",game_directions)

steps = {}


def print_map():
    for x in range(len(plane)):
        for y in range(len(plane[x])):
            cc = complex(x,y)
            if cc in steps:
                print(steps[cc], end="")

            else:
                print(plane[x][y], end="")
        print()

def find_next_coord(direction, current):

    if direction == "L":
        next_coord = complex(int(current.real), len(plane[int(current.real)]) - 1)
    if direction == "R":
        next_y = re.search("(#|\.)", "".join(plane[int(current.real)])).start()
        next_coord = complex(int(current.real), next_y)
    if direction == "U":
        vps = "".join(vertical_plane[int(current.imag)])
        next_coord = complex(max(vps.rindex("#"), vps.rindex(".")),int(current.imag))
    if direction == "D":
        next_coord = complex(min(vertical_plane[int(current.imag)].index("#"), vertical_plane[int(current.imag)].index(".")),int(current.imag))

    next_sign = plane[int(next_coord.real)][int(next_coord.imag)]

    if next_sign == "#":
        return current, direction, True
    else:
        return next_coord, direction, False

def find_side(coord):
    if coord.real < 50:
        if coord.imag < 100:
            return "F"
        else:
            return "R"
    elif coord.real < 100:
        return "BO"
    elif coord.real < 150:
        if coord.imag < 50:
            return "L"
        else:
            return "BA"
    else:
        return "T"

def new_find_next_coord(direction, current):
    side = find_side(current)
    match side:
        case "F":
            if direction == "L":
                next_coord, next_direction = complex(149-current.real % 50, 0), "R"
            elif direction == "U":
                next_coord, next_direction = complex(150+(current.imag % 50),0), "R"
        case "R":
            if direction == "U":
                next_coord, next_direction = complex(199,current.imag % 50), "U"
            elif direction == "R":
                next_coord, next_direction = complex(149-(current.real % 50),99), "L"
            elif direction == "D":
                next_coord, next_direction = complex(50 + (current.imag % 50),99), "L"
        case "BO":
            if direction == "L":
                next_coord, next_direction = complex(100, current.real % 50), "D"
            elif direction == "R":
                next_coord, next_direction = complex(49, 100 + (current.real % 50)), "U"
        case "BA":
            if direction == "R":
                next_coord, next_direction = complex(49 - current.real % 50, 149), "L"
            elif direction == "D":
                next_coord, next_direction = complex(150+ current.imag % 50, 49), "L"
        case "L":
            if direction == "U":
                next_coord, next_direction = complex(50 + current.imag % 50, 50), "R"
            elif direction == "L":
                next_coord, next_direction = complex(49 - current.real % 50, 50), "R"
        case "T":
            if direction == "L":
                next_coord, next_direction = complex(0, 50 + (current.real % 50)), "D"
            elif direction == "D":
                next_coord, next_direction = complex(0, 100 + current.imag % 50), "D"
            elif direction == "R":
                next_coord, next_direction = complex(149, 50 + current.real % 50), "U"

    next_sign = plane[int(next_coord.real)][int(next_coord.imag)]

    if next_sign == "#":
        return current, direction, True
    else:
        return next_coord, next_direction, False

def testing():
    flt, flb, flr = complex(0,50), complex(49, 50), complex(0, 99)
    assert new_find_next_coord("U", flt)[0] == complex(150,0)
    assert new_find_next_coord("L", flt)[0] == complex(149,0)
    assert new_find_next_coord("L", flb)[0] == complex(100, 0)
    assert new_find_next_coord("U", flr)[0] == complex(199,0)

    rlt, rrt, rlb, rrb =complex(0,100), complex(0,149), complex(49,100), complex(49, 149)
    assert new_find_next_coord("U", rlt)[0] == complex(199,0)
    assert new_find_next_coord("U", rrt)[0] == complex(199,49)
    assert new_find_next_coord("R", rrt)[0] == complex(149,99)
    assert new_find_next_coord("R", rrb)[0] == complex(100,99)
    assert new_find_next_coord("D", rrb)[0] == complex(99,99)
    assert new_find_next_coord("D", rlb)[0] == complex(50,99)


    bolt, bort, bolb, borb =  complex(50,50), complex(50,99), complex(99,50), complex(99,99)
    assert new_find_next_coord("L", bolt)[0] == complex(100,0)
    assert new_find_next_coord("L", bolb)[0] == complex(100,49)
    assert new_find_next_coord("R", bort)[0] == bort
    assert new_find_next_coord("R", borb)[0] == complex(49,149)

    bart, barb, balb = complex(100,99), complex(149,99), complex(149,50)
    assert new_find_next_coord("R", bart)[0] == complex(49,149)
    assert new_find_next_coord("R", barb)[0] == complex(0,149)
    assert new_find_next_coord("D", barb)[0] == complex(199,49)
    assert new_find_next_coord("D", balb)[0] == complex(150,49)

    llt, lrt, llb = complex(100,0), complex(100,49), complex(149,0)
    assert new_find_next_coord("L", llt)[0] == complex(49,50)
    assert new_find_next_coord("U", llt)[0] == complex(50,50)
    assert new_find_next_coord("U", lrt)[0] == complex(99,50)
    assert new_find_next_coord("L", llb)[0] == complex(0,50)

    tlt, trt, tlb, trb = complex(150,0), complex(150,49), complex(199,0), complex(199,49)
    assert new_find_next_coord("L", tlt)[0] == complex(0,50)
    assert new_find_next_coord("L", tlb)[0] == complex(0,99)
    assert new_find_next_coord("D", tlb)[0] == complex(0,100)
    assert new_find_next_coord("D", trb)[0] == complex(0,149)
    assert new_find_next_coord("R", trb)[0] == complex(149,99)
    assert new_find_next_coord("R", trt)[0] == complex(149,50)

def do_assignment(step_func):
    global current_direction

    current = complex(0, int(game_input[0].index(".")))
    for direction in game_directions:
        if direction.isnumeric():
            for _ in range(int(direction)):
                assert plane[int(current.real)][int(current.imag)] in ["."]
                steps[current] = current_direction
                next_coord = current + move[current_direction]
                if next_coord.real < 0 or next_coord.imag < 0:
                    next_sign = " "
                else:
                    try:
                        next_sign = plane[int(next_coord.real)][int(next_coord.imag)]
                    except:
                        next_sign = " "

                if next_sign == "#":
                    break
                elif next_sign == " ":
                    current, current_direction, should_break = step_func(current_direction, current)
                else:
                    current = next_coord

        if direction.isalpha():
            current_direction = adjust[current_direction][direction]

    facing_values = {"R" : 0, "D" : 1, "L" : 2, "U" : 3}
    print(f"Answer: {1000*int(current.real + 1) + 4 * int(current.imag + 1) + facing_values[current_direction]}")

do_assignment(find_next_coord)
do_assignment(new_find_next_coord)
