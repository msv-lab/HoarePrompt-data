def func_1(x1, x2, x3, y1, y2, y3):
    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    return area / 2
n = int(sys.stdin.readline())
Points = []
for i in range(n):
    (x, y) = map(int, sys.stdin.readline().split())
    Points.append([x, y])
maxx = 0
for i in range(n):
    for j in range(i + 1, n):
        x1 = Points[i][0]
        y1 = Points[i][1]
        x3 = Points[j][0]
        y3 = Points[j][1]
        maxx1 = 0
        maxx2 = 0
        for z in range(n):
            area = func_1(x1, y1, x3, y3, Points[z][0], Points[z][1])
            if area > 0:
                if area > maxx1:
                    maxx1 = area
            elif -area > maxx2:
                maxx2 = -area
        if maxx1 + maxx2 > maxx:
            maxx = maxx1 + maxx2
sys.stdout.write(str(maxx))