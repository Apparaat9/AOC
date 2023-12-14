
data = open('input/day14.txt').read().splitlines()
table_map = {complex(y,x) : data[y][x] for x in range(len(data[0])) for y in range(len(data))}
width, height = len(data[0]), len(data)

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
        for c in [-1, -1j, 1, 1j] if a else [-1]:
            for y in range(height) if c != 1 else reversed(range(height)):
                for x in range(width) if c != 1j else reversed(range(width)):
                    this_location = complex(y, x)
                    if table_map[this_location] == 'O':
                        while this_location + c in table_map and table_map[this_location + c] == '.':
                            table_map[this_location] = '.'
                            table_map[this_location + c] = 'O'
                            this_location += c
    return values

for n, t, a in [(1,3,0),(100, 100_000_000, 1)]:
    cycle = find_cycle(n, t, a)
    index = int(((t - n) / n) % len(cycle))
    print(f"Assignment {a+1}:\t {cycle[index]}")
