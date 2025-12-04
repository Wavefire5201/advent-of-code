#!/usr/bin/env python3


def gen(mx: list[list]):
    modified = [row[:] for row in mx]
    count = 0
    for i in range(len(mx)):
        for j in range(len(mx[i])):
            if mx[i][j] == "@":
                adjacent = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == 0 and y == 0:
                            continue
                        if 0 <= i + x < len(mx) and 0 <= j + y < len(mx[i]):
                            if mx[i + x][j + y] == "@":
                                adjacent += 1

                if adjacent < 4:
                    modified[i][j] = "."
                    count += 1

    return modified, count


with open("input.txt") as f:
    init = []
    count = 0
    gbcount = 0
    iter = 0

    # make initial board
    for line in f.readlines():
        init.append([i for i in line.strip()])

    cont = True
    while cont:
        new, c = gen(init)
        gbcount += c
        if c == 0:
            cont = False
        else:
            init = new

        if iter == 0:
            print(f"p1: {gbcount}")
        iter += 1

    print(f"p2: {gbcount}")
