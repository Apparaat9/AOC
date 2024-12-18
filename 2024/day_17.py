
import re

def function(opcode, operant, pointer):
    global A, B, C
    match opcode:
        case 0:
            A = A // 2**combo(operant)
        case 1:
            B = B ^ operant
        case 2:
            B = combo(operant) % 8
        case 3:
            if A: return operant
        case 4:
            B = B ^ C
        case 5:
            R.append(combo(operant) % 8)
        case 6:
            B = A // 2**combo(operant)
        case 7:
            C = A // 2**combo(operant)
    return pointer + 2

def combo(operant):
    match operant:
        case 1 | 2 | 3:
            return operant
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C

A, _, _, *P = map(int, re.findall(r'\d+', open('input/day_17.txt').read()))
R = []
counter = f = 0
power_counter = len(P) - 1
while P != R:
    A = a = (f + (8**power_counter) * counter) if counter else A
    B = C = pointer = 0
    R = []
    
    while pointer < len(P):
        pointer = function(P[pointer], P[pointer+1], pointer)

    if P[power_counter:] == R[power_counter:]:
        f = a
        power_counter -= 1
        counter = 0

    if not counter and power_counter == len(P) - 1:
        print(*R, sep=', ')
    counter += 1

print(a)


