with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    ar = 0
    for line in lines:
        x, y = line.split(",")
        for line in lines:
            j, k = line.split(",")
            g = (abs(int(x) - int(j)) + 1) * (abs(int(y) - int(k)) + 1)
            if g >= ar:
                ar = g

    print(ar)
