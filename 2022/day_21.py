import z3

def assignment1(game_input):
    failed = True
    while failed:
        failed = False
        for data in game_input:
            try:
                exec(data, globals())
            except:
                failed = True
    print(f"Answer: {root}")


def assignment2(game_input):

    new_input = ['humn = xxx', 'rnsd = vlzj']
    game_input = [x for x in game_input if x not in ['humn = 4977','root = rnsd + vlzj']]
    final_input = game_input + new_input

    for x in final_input:
        term = x.split()[0]
        exec(f"{term} = z3.Int('{term}')",globals())
    xxx = z3.Int('xxx')
    s = z3.Solver()

    for x in final_input:
        statement = x.replace('=', '==')
        exec(f"s.add({statement})")

    assert s.check() == z3.sat

    model = s.model()
    print(f"Answer: {model[xxx]}")

gm = open("input/day21_input.txt", "r").read().replace(':', " =").splitlines()
assignment1(gm)
assignment2(gm)
