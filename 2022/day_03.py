
game_input = open("input/day3_input.txt", "r").read().splitlines()

def get_value(character):
    value = ord(character)
    if value >= 97:
        return value - 96
    else:
        return value - 38

def first_assignment():
    score = 0
    for rucksack in game_input:
        halve = int(len(rucksack) / 2)
        first, second = rucksack[:halve], rucksack[halve:]
        prio_score = get_value(set(first).intersection(set(second)).pop())
        score += prio_score
    print(score)

def second_assignment():
    score = 0
    for i in range(3, len(game_input)+1, 3):
        first, second, third = game_input[i-3:i]
        prio_score = get_value(set(first).intersection(set(second).intersection(set(third))).pop())
        score += prio_score
    print(score)

first_assignment()
second_assignment()