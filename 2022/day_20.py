import copy


class CircularList:
    def __init__(self, l):
        self.len = len(l)
        self.tl = list(zip(range(0,len(l)),l))
        self.ml = copy.copy(self.tl)
        self.zero = [x for x in self.tl if not x[1]][0]

    def move_piece(self, piece):
        move = self.tl.index(piece) + piece[1] % (self.len - 1)
        if move >= self.len:
            move = move - self.len + 1
        self.tl.remove(piece)
        self.tl.insert(move, piece)

    def get_value(self, coords):
        move = coords % self.len + self.tl.index(self.zero)
        if move >= self.len:
            move = move - self.len
        return self.tl[move][1]


def do_assignment(data, multiplier, shuffles):
    original_list = [x * multiplier for x in data]

    cl = CircularList(original_list)
    for _ in range(shuffles):
        for i in cl.ml:
            cl.move_piece(i)

    answer = []
    for c in [1000, 2000, 3000]:
        answer.append(cl.get_value(c))
    print(f"Answer: {sum(answer)}"  )


game_input = list(map(int, open("input/day20_input.txt", "r").read().splitlines()))
do_assignment(game_input, 1, 1)
do_assignment(game_input, 811589153, 10)
