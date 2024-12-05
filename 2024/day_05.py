rules, updates = open('input/day_05.txt').read().split('\n\n')

rules = [x.split('|') for x in rules.split()]
updates = [x.split(',') for x in updates.split()]

def abide(update, rules) : return all(not (a in update and b in update) or update.index(a) < update.index(b) for a,b in rules)

c1, c2 = 0, 0
for update in updates:
    if abide(update, rules):
        c1 += int(update[len(update)//2])
    else:
        while not abide(update, rules):
            for a, b in rules:
                if not abide(update, [(a, b)]):
                    update.insert(update.index(a), update.pop(update.index(b)))
        c2 += int(update[len(update)//2])
print(c1, c2)