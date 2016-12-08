f = open("input.txt", "r")
triangles = map(lambda x : map(int, filter(lambda x: x != '', x.split())), f.read().split("\n"))
total = 0

for triangle in triangles:
    if len(triangle) != 3: continue
    if (triangle[0] < triangle[1] + triangle[2] and
        triangle[1] < triangle[0] + triangle[2] and
        triangle[2] < triangle[0] + triangle[1]):
        total += 1

print total
