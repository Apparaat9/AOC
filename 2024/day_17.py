
import re

def get_combo(n):
    if n < 4:
        return n
    elif n == 4:
        return A
    elif n ==  5:
        return B
    elif n == 6:
        return C
    elif n == 7:
        exit('NON VALID COMBO OPERANT 7')
    else:
        print('FAULTY COMBO')

def do_instruction(opcode, operant, pointer):
    global A,B,C,R
    if opcode == 0:
        A = A // 2**get_combo(operant)
        return pointer + 2
    if opcode == 1:
        B = B ^ operant
        return pointer + 2
    if opcode == 2:
        B = get_combo(operant) % 8
        return 2
    if opcode == 3:
        if A == 0:
            return pointer + 2
        return operant
    if opcode == 4:
        B = B ^ C
        return pointer + 2
    if opcode == 5:
        R.append(get_combo(operant) % 8)
        return pointer + 2
    if opcode == 6:
        B = A // 2**get_combo(operant)
        return pointer + 2
    if opcode == 7:
        C = A // 2**get_combo(operant)
        return pointer + 2

A, B, C, *P = map(int, re.findall(r'\d+', open('input/day_17.txt').read()))
R, pointer = [], 0

while pointer < len(P):
    pointer = do_instruction(P[pointer], P[pointer+1], pointer)
    
print(', '.join(map(str, R)))

R = []
counter = f = 0
power_counter = len(P) - 1
while P != R:
    B, C, pointer, R = 0, 0, 0, []
    A = a = f + (8**power_counter) * counter

    while pointer < len(P):
        pointer = do_instruction(P[pointer], P[pointer+1], pointer)

    if P[power_counter:] == R[power_counter:]:
        f = a
        power_counter -= 1
        counter = 0
    counter += 1

print(a)


