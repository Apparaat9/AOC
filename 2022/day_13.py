
def check_values(v1, v2, result):
    if isinstance(v1, int):
        if isinstance(v2, list):
            v1 = [v1]
        elif v1 > v2:
            return result + [0]
        elif v1 < v2:
            return result + [2]
        else:
            return result + [1]
    if v1 and isinstance(v1, list):
        if isinstance(v2, int):
            v2 = [v2]
        for i in range(max(len(v2),len(v1))):
            try:
                result += check_values(v1[i], v2[i], [])
                if result[-1] in [0,2]:
                    break
            except:
                if len(v1) > len(v2):
                    result += [0]
                else:
                    result += [2]
                break
    else:
        return result + [2] if v2 else result + [1]
    return result

def assigment_1(game_input):
    all_results = []
    for i in range(0, len(game_input), 2):
        list1, list2 = eval(game_input[i]), eval(game_input[i+1])
        all_results.append(all(check_values(list1, list2, [])))
    res = [i+1 for i, x in enumerate(all_results) if x]
    print(sum(res))


def assigment_2(game_input):
    all_lists = []
    signals = ['[[2]]','[[6]]']
    game_input += signals
    for i in range(len(game_input)):
        this_input = game_input[i].replace('[]','0').replace('[','').replace(']','').replace('10','_').replace(',','')
        all_lists.append([this_input,game_input[i]])
    all_lists = sorted(all_lists, key=lambda x: x[0])
    res = [i + 1 for i, x in enumerate(all_lists) if x[1] in signals]
    print(res[0] * res[1])

game_input = [x for x in open("input/day13_input.txt", "r").read().splitlines() if x]
assigment_1(game_input)
assigment_2(game_input)
