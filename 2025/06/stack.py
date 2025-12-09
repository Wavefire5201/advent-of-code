# stack approach for p2 after seeing visualization online

with open("input.txt") as f:
    lines = [line.strip("\n") for line in f.readlines()]

o = lines[4]  # operators

total = 0
group = True
current_op = o[0]

temp = []
group_temp = 0
current_group = []

for i in range(0, len(lines[0])):
    blank = 0
    for j in range(4):
        if lines[j][i] == " ":
            blank += 1
    if blank == 4:
        group = False
        group_temp = 1 if current_op == "*" else 0
        # print(i, temp, current_op)
        for t in temp:
            if current_op == "*":
                group_temp *= t
            elif current_op == "+":
                group_temp += t
        # print(group_temp)
        total += group_temp
    elif blank < 4 and not group:
        group = True
        temp = []
        current_op = o[i]
    if group:
        for _ in range(4):
            current_group.append(lines[_][i])
        temp.append(int("".join(current_group)))
        current_group = []

# account for last group
group_temp = 1 if current_op == "*" else 0
# print(temp, current_op)
for t in temp:
    if current_op == "*":
        group_temp *= t
    elif current_op == "+":
        group_temp += t
total += group_temp

print(total)
