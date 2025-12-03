with open("input.txt") as f:
    zero_cnt = 0
    p2 = 0
    lock_pos = 50  # starting dial pos
    for line in f.readlines():
        op, num = line[0], int(line[1:])
        for _ in range(num):
            if op == "L":
                lock_pos = (lock_pos - 1 + 100) % 100
            else:
                lock_pos = (lock_pos + 1) % 100
            if lock_pos == 0:
                p2 += 1

        # print(line.strip(), lock_pos)
        zero_cnt = zero_cnt + 1 if lock_pos == 0 else zero_cnt

print(zero_cnt)
print(p2)
