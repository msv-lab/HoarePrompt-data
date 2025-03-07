def func_1():
    r = list(map(int, input().split()))
    (n, m, x1, y1, x2, y2) = (r[0], r[1], r[2], r[3], r[4], r[5])
    if x2 <= x1:
        print('draw')
        return
    if (x2 - x1) % 2 != 0:
        if y1 == y2:
            print('Alice')
            return
        if y2 > y1:
            y1 += 1
            x1 += 1
        else:
            y1 -= 1
            x1 += 1
        if y1 == y2:
            print('Alice')
            return
        if y1 >= y2:
            a = y2 - 1
        else:
            a = m - y2
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if x2 <= x1 or x1 < 1 or x2 > n:
            print('draw')
            return
        if y2 <= y1:
            y2 = 1
            y1 -= a
            c = y1 - 1
        else:
            y2 = m
            y1 += a
            c = m - y1
        if b // 2 > a and abs(x2 - c) >= x1 + c and (1 <= y1 <= m) and (1 <= x1 <= n):
            print('Alice')
            return
        else:
            print('draw')
            return
    else:
        if y1 == y2:
            print('bob')
            return
        if y2 >= y1:
            a = y1 - 1
        else:
            a = m - y1
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if x2 <= x1 or x1 < 1 or x2 > n:
            print('draw')
            return
        if y1 <= y2:
            y1 = 1
            y2 -= a
            c = y2 - 1
        else:
            y1 = m
            y2 += a
            c = m - y2
        if b // 2 > a and abs(x2 - c) >= x1 + c and (1 <= y1 <= m) and (1 <= x1 <= n):
            print('bob')
            return
        else:
            print('draw')
            return
tt = int(input())
for _ in range(tt):
    func_1()