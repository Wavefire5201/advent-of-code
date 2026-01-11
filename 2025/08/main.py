def distance(x1, y1, z1, x2, y2, z2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5


with open("ex.txt") as f:
    lines = [line.strip() for line in f.readlines()]

for i in range(len(lines)):
    a = lines[i].split(",")
    x = int(a[0])
    y = int(a[1])
    z = int(a[2])
    for j in range(len(lines)):
        t = lines[j].split(",")
        _x = int(t[0])
        _y = int(t[1])
        _z = int(t[2])
        print(distance(x, y, z, _x, _y, _z))
