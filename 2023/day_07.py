from collections import Counter

data = [s.split() for s in open('input/day7.txt').read().splitlines()]
value_orders = {x : idx + 1 for idx, x in enumerate(['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'][::-1])}

def parse(x) : return x if x == 'JJJJJ' else x.replace("J", Counter(x.replace("J","")).most_common()[0][0])

def do_assignment(n):
    cards = [[x[0], parse(x[0]) if n else x[0], x[1]] for x in data]

    s = sorted(cards, key=lambda i: (
        len(i[1]) - len(set(i[1])),
        max(Counter(i[1]).values()),
        [value_orders[x] for x in i[0]]
    ))
    return sum((int(s[x][2]) * (x+1))for x in range(len(s)))

print(do_assignment(0))
print(do_assignment(1))