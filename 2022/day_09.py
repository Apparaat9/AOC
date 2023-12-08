game_input = open("input/day9_input.txt", "r").read().splitlines()

class Coords:
    def __init__(self):
        self.x = 0
        self.y = 0

    def xy(self):
        return self.x, self.y

class Rope:
    def __init__(self):
        self.head = Coords()
        self.tail = Coords()
        self.visits = {(0,0)}

    def move(self, side, direction):
        if direction == "L":
            side.x += -1
        elif direction == "R":
            side.x += 1
        elif direction == "U":
            side.y += 1
        elif direction == "D":
            side.y += -1
        self.adjust_tail(self.head, self.tail)
        self.add_visit(self.tail)

    def adjust_tail(self, head, tail):
        x_dif = abs(head.x - tail.x)
        y_dif = abs(head.y - tail.y)
        if x_dif > 1 and y_dif > 1:
            tail.x = int((head.x + tail.x) / 2)
            tail.y = int((head.y + tail.y) / 2)
        elif x_dif > 1:
            if y_dif:
                tail.y = head.y
            tail.x = int((head.x + tail.x) / 2)
        elif y_dif > 1:
            if x_dif:
                tail.x = head.x
            tail.y = int((head.y + tail.y) / 2)

    def add_visit(self, side):
        self.visits.add(side.xy())


def do_assignment(assignment):
    ropes = [Rope() for _ in range(10)]
    for action in game_input:
        direction, count = action.split()
        for i in range(int(count)):
            ropes[0].move(ropes[0].head, direction)
            if assignment:
                for y in range(1, len(ropes)):
                    ropes[y].adjust_tail(ropes[y - 1].head, ropes[y].head)
                    ropes[-1].add_visit(ropes[-1].head)
    print(len(ropes[assignment].visits))

do_assignment(0)
do_assignment(-1)