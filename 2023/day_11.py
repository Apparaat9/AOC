import itertools

def get_expanse_results(expanse, universe):
    insert_at = [idx for idx, row in enumerate(universe) if set(row) == {'.'}]
    offset = 0
    for x in insert_at:
        for i in range(expanse):
            universe.insert(x + offset, ['.'] * len(universe[0]))
        offset += expanse

    insert_at = [i for i in range(len(universe[0])) if set(universe[y][i] for y in range(len(universe))) == {'.'}]
    offset = 0
    for x in insert_at:
        for i in range(expanse):
            for y in range(len(universe)):
                universe[y].insert(x + offset, '.')
        offset += expanse

    galaxies = [(x,y) for x in range(len(universe[0])) for y in range(len(universe)) if universe[y][x] == '#']
    return [abs(l[0] - r[0]) + abs(l[1] - r[1]) for l, r in itertools.combinations(galaxies, 2)]

universe = [[x for x in y] for y in open('input/day11.txt').read().splitlines()]
zero, one = [get_expanse_results(x, universe) for x in [0,1]]
diff = [one[i] - zero[i] for i in range(len(zero))]
print(sum(one))
print(sum([zero[i] + (999_999 * diff[i]) for i in range(len(zero))]))