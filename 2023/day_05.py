import re

def find_scores(seeds):
    for row in data[2:]:
        next_seeds = set({})
        for mapping in re.findall(r"\d+ \d+ \d+", row):
            kept_seeds = set({})
            dest, src, length = map(int,mapping.split())

            while seeds:
                pair = seeds.pop()
                left_relevant = src <= pair[0] <= src+length
                right_relevant = src <= pair[1] <= src+length
                left_split = (pair[0], src - 1 if pair[0] < src else min(pair[1],  src+length))
                right_split = (left_split[1] + 1, pair[1])

                if right_relevant and left_relevant:
                    next_seeds |= {tuple((x + dest-src for x in left_split))}
                elif left_relevant:
                    next_seeds |= {tuple((x + dest-src for x in left_split))}
                    seeds |= {right_split}
                elif right_relevant:
                    next_seeds |= {tuple((x + dest-src for x in right_split))}
                    seeds |= {left_split}
                else:
                    kept_seeds |= {pair}
            seeds = kept_seeds
        seeds |= next_seeds
    return seeds

data = open('input/day5.txt').read().split(":")
seeds = list(map(int,re.findall(r"\d+", data[1])))

def do_assignment(n):
    seed_ranges = {(seeds[y], seeds[y]+seeds[y+1]) for y in range(0, len(seeds), 2)} if n else {(y,y) for y in seeds}
    return min([x[0] for x in find_scores(seed_ranges)])

print(do_assignment(0))
print(do_assignment(1))






