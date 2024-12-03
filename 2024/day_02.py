from itertools import combinations

data = [list(map(int, x.split())) for x in open('input/day_02.txt').read().splitlines()]

def check_diff(numbers):
    diff = list(map(lambda x,y: x-y, numbers[:-1], numbers[1:]))
    if not min(diff) < 0 < max(diff) and all(1 <= abs(x) <= 3 for x in diff):
            return 1
    return 0

c2 = [any(check_diff(x) for x in [numbers] + list(combinations(numbers, len(numbers) - 1))) for numbers in data].count(True)

print(sum(check_diff(x) for x in data), c2)