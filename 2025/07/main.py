with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

for r in range(len(lines)):
    for c in range(len(lines)):
        print(r, c)
