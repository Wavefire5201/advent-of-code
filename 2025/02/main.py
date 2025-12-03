with open("input.txt") as f:
    input = f.readline().split(",")
    p1 = 0
    p2 = 0
    for ids in input:
        start, end = ids.split("-")
        for id in range(int(start), int(end) + 1):
            id = str(id)
            if len(id) % 2 == 0:
                c = int(len(id) / 2)
                l, r = id[:c], id[c:]
                if l == r:
                    p1 += int(id)

            for i in range(len(id)):
                if id.count(id[:i]) * id[:i] == id:
                    # print(id)
                    if len(id) % 2 == 0:
                        p2 += int(id)
                        break
                    p2 += int(id)

    print(p1)
    print(p2)

# slow brute force solution lol
