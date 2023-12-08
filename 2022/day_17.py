
def plot_tetris(tetris, limits, limit=0):
    for y in reversed(range(int(max(limits['b'], limit)), int(limits['p'] + 1))):
        for x in range(limits['l'], limits['r'] + 1):
            if complex(x,y) in tetris:
                print("#",end='')
            else:
                print(".",end='')
        print('')
    print('')

def tetrify(gusts, shapes, rounds):
    gust_counter = 0
    moves = {'>': 1, '<': -1, 'v': 0 - 1j}
    limits = {"l": 0, "r": 6, "b": 0, "p": 0}
    tetris = set()

    for i in range(rounds):
        if i % (340_000) == 0 and i > 0:
            print(f"Total\t{i + 1}, within loop\t{gust_counter} for height\t {limits['p']}")
        falling = True
        cur_b = [x + (limits['p'] * 1j + 3j) for x in shapes[i % 5]]

        while falling:
            pot_b = [x + moves[gusts[gust_counter]] for x in cur_b]
            gust_counter = gust_counter + 1 if gust_counter != len(gusts) - 1 else 0
            if not set(pot_b).intersection(tetris) and pot_b[0].real >= limits['l'] and pot_b[-1].real <= limits['r']:
                cur_b = pot_b

            pot_b = [x + moves['v'] for x in cur_b]
            if set(pot_b).intersection(tetris) or min(x.imag for x in pot_b) < limits['b']:
                tetris |= set(cur_b)
                limits['p'] = max([limits['p']] + [x.imag + 1 for x in cur_b])
                falling = False
            cur_b = pot_b
    plot_tetris(tetris, limits)
    print(f"Reached {limits['p']} after {gust_counter} rounds!\n")

shapes = [[complex(2,0), complex(3,0), complex(4,0), complex(5,0)], # H_LINE
          [complex(2,1), complex(3,0), complex(3,1),complex(3,2), complex(4,1)], # CROSS
          [complex(2,0), complex(3,0), complex(4,0),complex(4,1),complex(4,2)], # _|
          [complex(2,0), complex(2,1),complex(2,2), complex(2,3)], # V_LINE
          [complex(2,0), complex(2,1), complex(3,0), complex(3,1)]] # SQUARE

gusts = [x for x in open("input/day17_input.txt").read()]

tetrify(gusts, shapes, 2022)

## For assigment 2, stop the script after a while and calculate stack duplication constant to get result
tetrify(gusts, shapes, 1_000_000_000_000)


