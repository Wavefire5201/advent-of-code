#!/usr/bin/env python3
with open("input.txt") as f:
    p1 = 0
    for bank in f.readlines():
        bank = bank.strip()
        a = int(bank[-2])
        b = int(bank[-1])
        start = 0
        for n in range(start, len(bank) - 1):
            v = int(bank[n])
            if v > a:
                a = v
                start = n

        # print(start)
        e = 0
        for n in range(start + 1, len(bank)):
            v = int(bank[n])
            if v > b:
                b = v
                e = n
        # print(e)

        # print(bank)
        # print(f"{a}{b}\n")
        p1 += int(f"{a}{b}")

    print(p1)

# p2
with open("input.txt") as q:
    p2 = 0
    for bank in q.readlines():
        bank = bank.strip()
        vals = []
        start = 0
        for i in range(12):
            # print(bank)
            # print(vals)
            # print(start)
            best = -1
            best_index = -1
            for n in range(start, len(bank) - (11 - i)):
                v = int(bank[n])
                if v > best:
                    best = v
                    best_index = n
            vals.append(str(best))
            start = best_index + 1

        # print(bank)
        # print(vals)
        p2 += int("".join(vals))

    print(p2)
