
rpc = {"A" : "rock", "B" : "paper", "C" : "scissors", "X": "rock", "Y" : "paper", "Z" : "scissors"}
losses = {"paper rock" : "lose", "scissors paper" : "lose", "rock scissors" : "lose"}
game_scores = {"draw" : 3, "win" : 6, "lose": 0}
type_scores = {"rock" : 1, "paper":2,"scissors":3}

result_map = {"X" : "lose", "Y" : "draw", "Z" : "win"}
options = {"rock","paper","scissors"}

game_input = open("input/day2_input.txt","r").read().splitlines()

def assignment_1():
    scores = 0
    for game in game_input:
        type1, type2 = [rpc[x] for x in game.split()]
        if type1 == type2:
            match_score = game_scores["draw"]
        elif f'{type1} {type2}' in losses.keys():
            match_score = game_scores["lose"]
        else:
            match_score = game_scores["win"]
        scores += match_score + type_scores[type2]
    print(scores)

def assignment_2():
    scores = 0
    for game in game_input:
        type1, result = rpc[game.split()[0]], result_map[game.split()[1]]
        if result == "draw":
            type_score = type_scores[type1]
        elif result == "lose":
            type_score = type_scores[[x.split()[1] for x in losses.keys() if x.split()[0] == type1][0]]
        else:
            type_score = type_scores[list(options.symmetric_difference({type1,[x.split()[1] for x in losses.keys() if x.split()[0] == type1][0]}))[0]]
        scores += game_scores[result] + type_score
    print(scores)

assignment_1()
assignment_2()