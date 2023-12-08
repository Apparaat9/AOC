import copy


class Coords():
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = ord(v)
        self.routes = set()

    def get(self):
        return (self.x, self.y)

    def __add__(self, other):
        return (self.x + other[0], self.y + other[1])

class Route():
    def __init__(self, start):
        self.coords = None
        self.seen = []
        self.done = False
        self.score = 0
        self.go_to(start)

    def split(self):
        return copy.deepcopy(self)

    def get_paths(self):
        if not self.done:
            return [self.coords + d for d in [(1,0), (-1,0), (0,-1), (0,1)]]
        return []

    def go_to(self, coords):
        coords.routes.add(self)
        self.coords = coords
        self.seen.append(self.coords)
        self.score += 1

class Map():

    def __init__(self, game_input, assignment):
        self.all_point = {}
        self.start = []
        self.end = None
        self.game_input = game_input
        self.init_map(assignment)

    def init_map(self, assignment):
        for i in range(len(self.game_input)):
            for j in range(len(self.game_input[i])):
                c = Coords(i, j, self.game_input[i][j])
                if c.v == ord('S') or (c.v == ord('a') and assignment == '2'):
                    c.v = ord('a')
                    self.start.append(c)
                if c.v == ord('E'):
                    c.v = ord('z')
                    self.end = c
                self.all_point[f"{i}{j}"] = c

    def plot_map(self, coords):
        counter = 0
        for i in range(len(self.game_input)):
            for j in range(len(self.game_input[i])):
                if (i,j) in coords:
                    if counter % 2 == 0:
                        print(f'-', end='')
                    else:
                        print(f'*',end='')
                    counter += 1
                else:
                    print(f"{self.game_input[i][j]}", end='')
            print('')


    def get(self, tup):
        key = f"{tup[0]}{tup[1]}"
        if key in self.all_point:
            return self.all_point[key]
        else:
            return Coords(0,0,'€')

def solve_map(m):
    found = False
    all_routes = [Route(start) for start in m.start]

    while not found:
        new_routes = []
        for route in all_routes:
            viable = [path for path in route.get_paths() if route.coords.v - m.get(path).v >= -1 and not path in route.seen]
            for path in viable:
                point = m.get(path)
                other_scores = [r.score for r in point.routes]
                if other_scores and min(other_scores) <= route.score + 1:
                    pass
                else:
                    new_route = route.split()
                    new_route.go_to(point)
                    if point == m.end:
                        found = True
                        break
                    new_routes.append(new_route)
        all_routes = new_routes

    m.plot_map([x.get() for x in route.seen])
    print(f"Steps required: {new_route.score - 1}")

game_input = [x for x in open("input/day12_input.txt", "r").read().splitlines()]

m = Map(game_input, assignment='1')
solve_map(m)

m = Map(game_input, assignment='2')
solve_map(m)

