f = open("input.txt", "r");
instructions = f.read().split("\n")
pos = [2, 2] # y, z
code = []
for instruction in instructions:
    currentMove = None
    while len(instruction) > 0:
        currentMove = instruction[:1]
        instruction = instruction[1:]
        if (currentMove == "L" and pos[1] > 1):
            pos[1] -= 1
        if (currentMove == "R" and pos[1] < 3):
            pos[1] += 1
        if (currentMove == "U" and pos[0] > 1):
            pos[0] -= 1
        if (currentMove == "D" and pos[0] < 3):
            pos[0] += 1

    code += [3 * (pos[0] - 1) + pos[1]]

print code
