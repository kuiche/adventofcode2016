f = open("input.txt", "r")
instructions = f.read().split(", ")
position = [0, 0] # Start coords
direction = [1, 0] # NORTH

visited = set([str(position)])
firstRepeat = None

for instruction in instructions:
    turn = 1 if instruction[:1] == "R" else -1
    distance = int(instruction[1:])


    print "turning " + instruction[:1]
    print "direction was", direction
    direction = [direction[1] * turn, -direction[0] * turn] # New direction vector
    print "new direction", direction

    position[0] += (distance * direction[0])
    position[1] += (distance * direction[1])

    if firstRepeat == None:
        if str(position) in visited:
            firstRepeat = str(position)
        else:
            visited |= set([str(position)])

    print distance, "moved, new position is", position

print "final position ", position, "total distance", abs(position[0]) + abs(position[1]), "first repeat", firstRepeat
