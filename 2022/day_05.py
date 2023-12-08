import itertools

game_input = open("input/day5_input.txt", "r").read().splitlines()
split_index = game_input.index('')
stacks = game_input[:split_index]
moves = game_input[split_index + 1:]

def init_stacks(data):
    ordata = list(map(list, itertools.zip_longest(*data, fillvalue=None)))
    stacks = {}
    for stack in ordata:
        stack = stack[::-1]
        if stack[0] and stack[0].isnumeric():
            stacks[stack[0]] = []
            for container in stack[1:]:
                if container and container != ' ':
                    stacks[stack[0]].append(container)
    return stacks

def do_moves_1(stacks, moves, assignment):
    for move in moves:
        number, stack_from, stack_to = move.split(' ')[1::2]
        storage = []
        for i in range(int(number)):
            storage.append(stacks[str(stack_from)].pop())

        for crate in storage[::assignment]:
            stacks[str(stack_to)].append(crate)

    print("".join([stacks[key].pop() for key in stacks]))

stack_1 = init_stacks(stacks)
do_moves_1(stack_1, moves, assignment=1)
stack_2 = init_stacks(stacks)
do_moves_1(stack_2, moves, assignment=-1)


