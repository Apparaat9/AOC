import sys

game_input = [map(int, x.split(',')) for x in open('input/day18_input.txt', 'r').read().splitlines()]
game_input = [tuple(x) for x in game_input]

directions = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

min_x = min_y = min_z =  sys.maxsize
max_x = max_y = max_z = -sys.maxsize


def set_maxes():
    global min_x, max_x, min_y, max_y, min_z, max_z
    for coord in game_input:
        min_x = min(min_x, coord[0])
        max_x = max(max_x, coord[0])
        min_y = min(min_y, coord[1])
        max_y = max(max_y, coord[1])
        min_z = min(min_z, coord[2])
        max_z = max(max_z, coord[2])


def get_group_score(group, control_group):
    final = 0
    for coords in group:
        score = 6
        for dir in directions:
            neighbour = tuple(sum(x) for x in zip(coords, dir))
            if neighbour in control_group:
                score -= 1
        final += score
    return final


def get_all_possible():
    coords = []
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                coords.append(tuple((x, y, z)))
    return coords


def get_neighbours(point):
    n = []
    for dir in directions:
        n.append(tuple(sum(x) for x in zip(point, dir)))
    return n


def get_ranges(point):
    nx, ny, nz = [], [], []
    px, py, pz = point[0], point[1], point[2]
    for x in range(min_x, max_x + 1):
        nx.append(tuple(sum(xl) for xl in zip((0,py, pz), (x, 0, 0))))
    for y in range(min_y, max_y + 1):
        ny.append(tuple(sum(yl) for yl in zip((px,0,pz), (0,y, 0))))
    for z in range(min_z, max_z + 1):
        nz.append(tuple(sum(zl) for zl in zip((px, py, 0), (0, 0, z))))
    return [nx, ny, nz]


def find_bubbles(control_group, playing_field):
    holes = set()
    for ph in playing_field:
        if ph in control_group: continue
        ranges = get_ranges(ph)
        boxed = True
        for r in ranges:
            if ph in r:
                back, front = r[:r.index(ph)], r[r.index(ph)+1:]
                if not any([x in control_group for x in back]) or not any([x in control_group for x in front]):
                    boxed = False
                    break
            else:
                boxed = False
                break
        if boxed:
            holes.add(ph)
    return holes


def create_groups(super_group):
    group_sets = []
    for p1 in super_group:
        for p2 in get_neighbours(p1):
            if p2 in super_group:
                potential = []
                succes= False
                for i in range(len(group_sets)):
                    if p1 in group_sets[i] or p2 in group_sets[i]:
                        potential.append(i)
                        succes = True
                if not succes:
                    group_sets.append({p1, p2})
                elif succes:
                    if len(potential) == 1 or potential[0] == potential[1]:
                        group_sets[potential[0]].add(p1), group_sets[potential[0]].add(p2)
                    elif len(potential) == 2:
                        group1 = group_sets.pop(potential[0])
                        if potential[0] < potential[1]: potential[1] -= 1
                        group2 = group_sets.pop(potential[1])
                        new_group = set(list(group1) + list(group2))
                        new_group.add(p1), new_group.add(p2)
                        group_sets.append(new_group)
        if not any(p in super_group for p in get_neighbours(p1)):
            group_sets.append({p1})
    return group_sets


def do_task():
    set_maxes()
    playing_field = get_all_possible()

    score = get_group_score(game_input, game_input)
    pot_bubbles = find_bubbles(game_input, playing_field)
    bubble_groups = create_groups(pot_bubbles)
    final_bubbels = [x for x in bubble_groups if not get_group_score(x, set(x) | set(game_input))]
    fbs = [get_group_score(x, x) for x in final_bubbels]

    print(f"Assignment 1: {score}")
    print(f"Assignment 2: {score - sum(fbs)}")


do_task()