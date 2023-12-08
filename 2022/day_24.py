def calc_coord(coord):
    global moves

    new_coord = coord[0] + moves[coord[1]][0]
    if (0 < new_coord.real < limits[0] and 0 < new_coord.imag < limits[1]):
        return [new_coord, coord[1]]
    else:
        return [coord[0] + moves[coord[1]][1], coord[1]]


def add_seen(seen, blizzard, goal):
    global limits

    bs = {x[0] for x in blizzard}
    new_seen = set()
    for coord in seen:
        cm, cp, rm, rp, c, r = coord.imag - 1, coord.imag + 1, coord.real - 1, coord.real + 1, coord.imag, coord.real
        neighbours = {x for x in [complex(r,cm),complex(r,cp), complex(rm,c),complex(rp,c)] if (0 < x.real < limits[0] and 0 < x.imag < limits[1]) or x == goal}
        valid = neighbours - bs
        new_seen = new_seen | valid
    return new_seen | (seen - bs)


def blow(blizzards, seen):
    global limits
    for y, v in enumerate(game_input):
        for x, t in enumerate(v):
            if 0 < y < limits[1] and 0 < x < limits[0]:
                if complex(x,y) in [x[0] for x in blizzards]:
                    print("@",end="")
                elif complex(x,y) in seen:
                    print("X", end="")
                else:
                    print(".",end="")
            else:
                if complex(x,y) not in [start, end]:
                    print("#",end="")
                else:
                    print(".",end="")
        print()
    print()


def do_assignment(goal, blizzards):
    global start

    seen = {start}
    counter = 0
    while goal:
        blizzards = [calc_coord(b) for b in blizzards]
        seen = add_seen(seen, blizzards, goal[0])
        if goal[0] in seen:
            seen = {goal[0]}
            goal.pop(0)
        counter += 1

    print(f"Finished Goals In: {counter} ticks")

game_input = [[*x] for x in open("input/day24_input.txt", "r").read().splitlines()]

limits = [len(game_input[0]) - 1, len(game_input) - 1]
start, end = complex(1,0), complex(limits[0] - 1, limits[1])

moves = {"^": (-1j, 1j*(limits[1]-2)),
         "v": (1j, -1j*(limits[1]-2)),
         "<": (-1, 1*(limits[0]-2)),
         ">": (1, -1*(limits[0]-2))}

blizzard = [(complex(x,y),t) for y, v in enumerate(game_input) for x,t in enumerate(v) if t not in ["#","."]]

do_assignment([end], blizzard)
do_assignment([end, start, end], blizzard)