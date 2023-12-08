game_input = open("input/day8_input.txt", "r").read().splitlines()

forrest_h = [list(x) for x in game_input]
forrest_v = list(map(list, zip(*forrest_h)))


def assignment_one(forrest_h, forrest_v):
    score = len(forrest_h[0]) * 2 + (len(forrest_h[0]) - 2) * 2
    for t in range(len(forrest_h[1:-1])):
        for i in range(len(forrest_h[t+1])-2):
            check_left = max(forrest_h[t+1][:i+1])
            check_right = max(forrest_h[t+1][i+2:])
            check_top = max(forrest_v[i+1][:t+1])
            check_bottom = max(forrest_v[i+1][t+2:])
            if min([check_left, check_right, check_top, check_bottom]) < forrest_h[t+1][i+1]:
                score += 1
    print(score)


def get_score(v, line):
    score = 0
    for t in line:
        score += 1
        if int(t) >= int(v):
            break
    return score


def assigment_two(forrest_h, forrest_v):
    score = 0
    for t in range(len(forrest_h[1:-1])):
        for i in range(len(forrest_h[t+1])-2):
            current = forrest_h[t+1][i+1]
            check_left = forrest_h[t+1][:i+1]
            check_right = forrest_h[t+1][i+2:]
            check_top = forrest_v[i+1][:t+1]
            check_bottom = forrest_v[i+1][t+2:]

            s_l = get_score(current, check_left[::-1])
            s_r = get_score(current, check_right)
            s_t = get_score(current, check_top[::-1])
            s_b = get_score(current, check_bottom)

            score = max(score, s_l * s_r * s_t * s_b)
    print(score)

assignment_one(forrest_h, forrest_v)
assigment_two(forrest_h, forrest_v)
