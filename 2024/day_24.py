from collections import defaultdict

gates, npin = open('input/day_24.txt').read().split('\n\n')

ins_dict = defaultdict(set)
for operation in npin.split('\n'):
    o, t = operation.split(' -> ')
    ins_dict[t] = o

def get_byte_string(i):
    n = '0' * (45-len(format(i, 'b'))) + format(i, 'b')
    return n[::-1]

def get_variables(t):
    return [f'{t}{0 if i < 10 else ""}{i}' for i in range(0,45)]

def get_structure(k, d=0):
    if k not in ins_dict:
        return []
    a, i, b = ins_dict[k].split()
    return sorted([(k,i,d)] + get_structure(a, d+1) + get_structure(b, d+1), key=lambda x: x[2])

def run_code(n, ins):
    bn = get_byte_string(n)
    xs = get_variables('x')
    ys = get_variables('y')
    zs = get_variables('z')

    [exec(f'{xs[i]}={bn[i]}') for i in range(0,45)]
    [exec(f'{ys[i]}={bn[i]}') for i in range(0,45)]

    instructions = []
    for gate in ins.split('\n'):
        a, o, b, _, t = gate.split()
        o = o.replace("XOR","^").replace("OR","|").replace("AND","&")
        exec_string = f'{t} = locals()["{a}"] {o} locals()["{b}"]'
        instructions.append(exec_string)

    while instructions:
        i = instructions.pop(0)
        try:
            exec(i)
        except:
            instructions.append(i)

    binary = [str(locals()[x]) for x in zs[::-1]]
    ans = int(''.join(binary),2)
    return bool(n+n==ans)

zs = get_variables('z')
for idx, i in enumerate((2**p for p in range(0, 44))):
    if not run_code(i, npin):
        for s in [idx-1, idx, idx+1]:
            for x in get_structure(zs[s])[:7]:
                print(f'{x[2]*"\t"}{x[0]} - {x[1]}')
            print()
        exit()