from functools import cache

towels, designs = open('input/day_19.txt').read().split('\n\n')

@cache
def check_pattern(p):
    if not p: return 1 
    return sum([check_pattern(p.removeprefix(sub)) for sub in towels.split(', ') if p.startswith(sub)])

r = [check_pattern(d) for d in designs.split()]
print(len(r) - r.count(0))
print(sum(r))
