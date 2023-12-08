game_input = open("input/day4_input.txt", "r").read().splitlines()

assignment_1 = 0
assignment_2 = 0

for data in game_input:
    sections = [x.split('-') for x in  data.split(',')]
    range1, range2 = [list(range(int(x[0]),int(x[1]) + 1)) for x in sections]
    intersect = len(list(set(range1).intersection(range2)))
    if intersect >= len(range1) or intersect >= len(range2):
        assignment_1 += 1
    if intersect >= 1:
        assignment_2 += 1

print(assignment_1)
print(assignment_2)
