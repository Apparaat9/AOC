
data = list(map(lambda x:  list(map(int, x.split())), open('input/day9.txt').read().splitlines()))

def get_sequence(list):
    global a
    if len(set(list)) == 1:
        return list[0] if a else list[-1]
    new_list = [list[i+1] - list[i] for i in range(len(list[:-1]))]
    return list[0] - get_sequence(new_list) if a else list[-1] + get_sequence(new_list)

a = 0
print(sum(get_sequence(seq) for seq in data))
a = 1
print(sum(get_sequence(seq) for seq in data))