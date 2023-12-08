import z3

mapping = {"-1": "-", "-2": "=", "-" : -1, "=" : -2}
game_input = [[*x] for x in open("input/day25_input.txt").read().splitlines()]
game_input = [list(zip(x,list(range(len(x)))[::-1])) for x in game_input]


def parse_snafu(sign, pentamal):
    if sign in mapping:
        return mapping[sign] * (5**pentamal)
    else:
        return int(sign) * (5**pentamal)


def solve_snafu(integer, n=20):
    s = z3.Solver()
    ex = ""
    for x in range(n):
        s.add(-2 <= z3.Int(x), z3.Int(x) <= 2)
        ex += f"(z3.Int({x})*5**{x})+"
    ex = f"s.add({ex[:-1]} == {integer})"
    exec(ex)
    s.check()
    answer = [x[0] if x[0] not in mapping else mapping[x[0]] for x in sorted([(str(s.model()[point]),str(point)) for point in s.model().decls()], key=lambda x:int(x[1].split("!")[-1]))]
    return ''.join(answer[::-1])


def do_assignment():
    fr = []
    for snafu in game_input:
        results = [parse_snafu(*x) for x in snafu]
        fr.append(sum(results))
    print(f"Snafu:\t{sum(fr)}\t->\t{solve_snafu(sum(fr))}")


do_assignment()