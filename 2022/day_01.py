data = open("input/day1_input.txt", "r").read().splitlines()
results = []
subresult = 0

for number in data:
    if number:
        subresult += int(number)
    else:
        results.append(subresult)
        subresult = 0

print(f"Assignment 1:\t{max(results)}")

result = sum(sorted(results, reverse=True)[:3])
print(f"Assigment 2:\t{result}")
