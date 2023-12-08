

def parse_game_input(game_input):
    elfs, positions = [], set()
    for i in range(len(game_input)):
        for y in range(len(game_input[i])):
            if game_input[i][y] == "#":
                pos = complex(i,y)
                elfs.append(Elf(pos))
                positions.add(pos)
    return elfs, positions

def check_on_elves(elfs, score_only=False):
    elf_pos = [[x.pos.real, x.pos.imag] for x in elfs]
    real, imag = [x[0] for x in elf_pos], [x[1] for x in elf_pos]
    min_x, max_x = int(min(real)), int(max(real))
    min_y, max_y = int(min(imag)), int(max(imag))
    counter = 0
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            if [x,y] in elf_pos:
                if not score_only: print("#",end="")
            else:
                if not score_only: print(".",end="")
                counter += 1
        if not score_only: print("")
    print(f"Final Empty Tiles: {counter}\n")

class Elf():
    def __init__(self, pos):
        self.pos = pos
        self.moves = [[-1+0j,-1+1j,-1+-1j],
                      [1+0j,1+1j,1+-1j],
                      [0+-1j,-1+-1j,1+-1j],
                      [0+1j,-1+1j,1+1j]]

    def move(self, move):
        if isinstance(move,complex):
            positions.remove(self.pos)
            positions.add(move)
            self.pos = move
        self.moves.append(self.moves.pop(0))

    def check_pos(self):
        all_pos = [all(t + self.pos not in positions for t in x) for x in self.moves]
        if all(all_pos) or not any(all_pos):
            return elf_moves[""].append(self)
        move = self.pos + self.moves[all_pos.index(True)][0]
        if move not in elf_moves:
            elf_moves[move] = [self]
        elif elf_moves[move] is []:
            elf_moves[""].append(self)
        else:
            elf_moves[""] += elf_moves[move]
            elf_moves[""].append(self)
            elf_moves[move] = []



game_input = [[*x] for x in open("input/day23_input.txt", "r").read().split()]

elf_moves = {"" : []}
elfs, positions = parse_game_input(game_input)

def do_assignment(turns):
    global elf_moves, elfs

    for _ in range(turns):
        for elf in elfs:
            elf.check_pos()
        if len(elfs) == len(elf_moves[""]):
            print(f"No More Moves on: {_ + 1}")
            break
        for k, v in elf_moves.items():
            for e in v:
                e.move(k)
        elf_moves = {"" : []}

    check_on_elves(elfs, score_only=True)

do_assignment(10)
do_assignment(2_000)

