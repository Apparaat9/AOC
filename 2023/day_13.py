def get_mirror_or_smudges(pattern, task):
    for i in range(1, int(len(pattern[0]) / 2) + 1):
        if [r[0:i] == r[i:i+i][::-1] for r in pattern].count(False) == task:
            return i
        if [r[::-1][0:i] == r[::-1][i:i+i][::-1] for r in pattern].count(False) == task:
            return len(pattern[0]) - i

data = open('input/day13.txt').read().split('\n\n')

for t in [0, 1]:
    result = 0
    for pattern in data:
        if hr := get_mirror_or_smudges(pattern.split(), t):
            result += hr
        else:
            result += get_mirror_or_smudges([''.join(x) for x in zip(*pattern.split())], t) * 100
    print(f"Assignment {t + 1}:\t{result}")