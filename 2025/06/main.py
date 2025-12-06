with open("input.txt") as f:
    nums = []
    ops = []
    p1 = 0
    p2 = 0
    for line in f.readlines():
        line = line.strip()
        input = line.split()
        if len(input) < 1:
            continue
        if input[0].isnumeric():
            nums.append(input)
        else:
            ops = input

    # p1
    for i, op in enumerate(ops):
        # print(i, op)
        sum = 0 if op == "+" else 1
        cpod = []
        for j in range(len(nums)):
            num = int(nums[j][i])
            cpod.append(num)
            if op == "+":
                sum += num
            elif op == "*":
                sum *= num

        # p2
        new = []
        for c in range(len(str(max(cpod))) - 1, -1, -1):
            t = []
            for num in cpod:
                num = str(num)
                try:
                    # print(num, c, num[c])
                    t.append(num[c])
                except IndexError:
                    continue
            # print(t)
            new.append(int("".join(t)))

        fsum = 0 if op == "+" else 1
        print(new)
        for f in new:
            f = int(f)
            if op == "+":
                fsum += f
            elif op == "*":
                fsum *= f
        print(op, fsum)
        p1 += sum
        p2 += fsum

    print(p1)
    print(p2)
