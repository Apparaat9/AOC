import re

data = map(lambda x : x.replace(':','|').split('|'), open('input/day4.txt').readlines())
cards = {n.split()[-1] :len(set(re.findall(r'\d+', x)) & set(re.findall(r'\d+', y))) for n, x, y in data}
n_cards = {v : 1 for v in cards.keys()}

def do_assignment():
    for k, v in cards.items():
        for n in range(n_cards[k]):
            for i in range(int(k) + 1,int(k) + 1 + v):
                n_cards[str(i)] += 1
    return sum(n_cards.values())

print(sum(2**(v-1) for v in cards.values() if v))
print(do_assignment())
