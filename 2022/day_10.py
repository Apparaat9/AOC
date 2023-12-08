game_input = open("input/day10_input.txt", "r").read().splitlines()
data = [[0,int(x.split()[1])] if x != 'noop' else [0] for x in game_input]
data = [x for y in data for x in y]

def assignment_one():
    points = [20, 60, 100, 140, 180, 220]
    result = sum([(1 + sum(data[:p - 1])) * p for p in points])
    print(result)

def assignment_two():
    output = ""
    for i in range(240):
        cv = 1+sum(data[:i])
        if i % 40 in range(cv-1, cv+2):
            output += "#"
        else:
            output += "."

    start, wide = 0, 40
    for _ in range(6):
        print(output[start:wide])
        start = wide
        wide = wide + 40

assignment_one()
assignment_two()


