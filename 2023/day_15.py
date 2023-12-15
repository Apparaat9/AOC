import functools, collections

get_hash = lambda d: functools.reduce(lambda a, b: (a+b)*17 % 256, [ord(y) for y in d], 0)
data = open('input/day15.txt').read().strip().split(",")
print(f"Assignment 1:\t{sum([get_hash(d) for d in data])}")

boxes = collections.defaultdict(list)
for c in data:
    label, number = c.split('=') if '=' in c else c.split('-')
    box_code = get_hash(label)
    if idx := [idx for idx, k in enumerate(boxes[box_code]) if k[0] == label]:
        if number:
            boxes[box_code][idx[0]][1] = number
        else:
            del boxes[box_code][idx[0]]
    elif number:
        boxes[box_code].append([label, number])

r = [(k + 1) * (idx + 1) * int(box[1]) for k in boxes for idx, box in enumerate(boxes[k])]
print(f"Assignment 2:\t{sum(r)}")