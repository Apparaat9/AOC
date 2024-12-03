import re

def mul(x,y): return x*y

data = open("input/day_03.txt").read()
multis = re.findall(r'mul\(\d+,\d+\)', data)
print(sum(eval(x) for x in multis))

dodontmultis = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", data)
do = True
r = 0
for x in dodontmultis:
    if x == 'do()':
        do = True
    elif x == "don't()":
        do = False
    elif 'mul' in x and do:
        r += eval(x)
print(r)

