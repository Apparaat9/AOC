
import copy

turn = {'^' : '>', '>' : 'v', 'v' : '<', '<' : '^'}
step = {'^' : -1, '>' : 1j, '<' : -1j, 'v' : 1}


def get_data():
    m = {complex(i, t) : y for i, x in enumerate(open('input/day_06.txt').read().split()) for t, y in enumerate(x)}
    start = [k for k in m if m[k] == '^'][0]
    return m, start

def do_obstacle_walk(field, current, direction):
    field[current + step[direction]] = '#'

    while True:
        next = current + step[direction]
        
        while next in field and field[next] == '#':
            direction = turn[direction]
            next = current + step[direction]
        
        if next not in field:
            return 0     
        elif direction in field[next]:
            return 1
        
        current = next
        field[current] += direction


def main():
    field, current = get_data()
    direction = '^'
    seen = set()
    obstacles = 0
    while True:
        seen.add(current)
        next = current + step[direction]

        while field[next] == '#':
            direction = turn[direction]
            next = current + step[direction]

        if next not in field:
            return len(seen), obstacles
        if next not in seen:
            obstacles +=  do_obstacle_walk(copy.deepcopy(field), current, direction)

        current = next
        field[current] += direction

print(main())

