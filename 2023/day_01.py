import re

data = open("input/day1.txt","r").read().splitlines()
word_map = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six": "6", "seven" : "7", "eight" : "8", "nine" : "9"}
regex = "|".join(word_map.keys()) + "|\d"

def do_assignment(n):
    results = []
    for d in data:
        r = re.findall(fr"(?=({regex}))" if n else r"\d", d)
        r2 = [x if x.isnumeric() else word_map[x] for x in r] if n else [r[0],r[-1]]
        results.append(int(r2[0] + r2[-1]))
    return sum(results)

print(do_assignment(0))
print(do_assignment(1))