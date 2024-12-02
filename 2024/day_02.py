from itertools import combinations

data = [list(map(int, x.split())) for x in open('input/day_02.txt').read().splitlines()]

def check_diff(numbers):
    diff = list(map(lambda x,y: x-y, numbers[:-1], numbers[1:]))
    if not min(diff) < 0 < max(diff) and all(1 <= abs(x) <= 3 for x in diff):
            return 1
    return 0

c = 0
for numbers in data:
    candidates = [numbers] + list(combinations(numbers, len(numbers) - 1))
    if any(check_diff(x) for x in candidates):
        c += 1
print(c)