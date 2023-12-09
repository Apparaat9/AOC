
data = [[int(x) for x in l.split()] for l in open('input/day9.txt').read().splitlines()]

def get_sequence(list):
    if len(set(list)) == 1:
        return list[-1]
    new_list = [list[i+1] - list[i] for i in range(len(list[:-1]))]
    return list[-1] + get_sequence(new_list)

print(sum(get_sequence(seq) for seq in data))
print(sum(get_sequence(seq[::-1]) for seq in data))