game_input = open("input/day6_input.txt", "r").read().splitlines()[0]

def check_string(data, n):
    data = [x for x in data]
    for i in range(n, len(data)):
        check = {x for x in data[i-n:i]}
        if len(check) == n:
            print(i)
            break

check_string(game_input, 4)
check_string(game_input, 14)