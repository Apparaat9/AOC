
data = open('input/day14.txt').read().splitlines()
width, height = len(data[0]), len(data)
table_map = {complex(y,x) : data[y][x] for x in range(width) for y in range(height)}

def get_score():
    return sum([height - int(k.real) for k, v in table_map.items() if v == 'O'])

def get_map():
    for y in range(height):
        for x in range(width):
            print(table_map[complex(y,x)], end='')
        print('')

def find_cycle(n, t, a):
    values = []
    for i in range(0, t):
        if i and i % n == 0:
            values.append(get_score())
            if len(values) > 1 and values[0] == values[-1]:
                return values[:-1]
        for d in [-1, -1j, 1, 1j] if a else [-1]:
            for y in range(height) if d != 1 else reversed(range(height)):
                for x in range(width) if d != 1j else reversed(range(width)):
                    this_location = complex(y, x)
                    if table_map[this_location] == 'O':
                        while this_location + d in table_map and table_map[this_location + d] == '.':
                            table_map[this_location] = '.'
                            this_location += d
                        table_map[this_location] = 'O'
    return values

for n, t, a in [(1,3,0),(100, 100_000_000, 1)]:
    cycle = find_cycle(n, t, a)
    index = int(((t - n) / n) % len(cycle))
    print(f"Assignment {a+1}:\t {cycle[index]}")
