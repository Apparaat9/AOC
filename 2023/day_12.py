import functools

@functools.cache
def check_set(row, tups):
    if len(tups) == 0 and all(i in ['.', '?'] for i in row):
        return 1
    elif len(tups) == 0 and not all(i in ['.', '?'] for i in row):
        return 0

    this_tup = tups[0]
    next_tups = tups[1:]

    results = 0
    for i in range(len(row) - this_tup - len(next_tups) - sum(next_tups) + 1):
        option = f"{i * '.'}{'#' * this_tup}{'.' if next_tups else ''}"
        if all(row[i] == option[i] for i in range(len(option)) if row[i] != '?'):
            results += check_set(row[len(option):], next_tups)
    return results

data = list(map(lambda x :x.split(), open('input/day12.txt').read().splitlines()))

for x in [1,5]:
    results = 0

    for row, tup in data:
        row = f'{row}?' * x
        tup = f'{tup},' * x
        tup = tuple(map(int, tup[:-1].split(',')))
        results += check_set(row[:-1], tup)

    print(results)

