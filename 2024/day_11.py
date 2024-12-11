from functools import cache

stones = [x for x in open('input/day_11.txt').read().split()]

@cache
def check_stone(stone, n):
    if n == N:
        return 1
    if stone == '0':
        return check_stone('1', n+1)
    elif not len(stone) % 2:
        return check_stone(stone[:len(stone)//2], n+1) + check_stone(str(int(stone[len(stone)//2:])), n+1)
    else:
        return check_stone(str(int(stone)*2024), n+1)

N = 25
print(sum(x for x in [check_stone(s, 0) for s in stones]))
check_stone.cache_clear()
N = 75
print(sum(x for x in [check_stone(s, 0) for s in stones]))

##### -- Momument of my own brilliant but unsuccessful, "smarter than cache" cache.
    # from collections import defaultdict 
    # from bisect import bisect
    # cache_dict = defaultdict(dict)
    # if stone in cache_dict and bisect(list(cache_dict[stone]), N-n):
    #     target = bisect(list(cache_dict[stone]), N-n)
    #     if target:
    #         target = list(cache_dict[stone])[target-1]
    #         for stone in cache_dict[stone][target]:
    #             this_result += check_stone(stone, n + target)
    # if stone not in cache_dict or N - n not in cache_dict[stone]:
    #   cache_dict[stone][N - n] = this_result