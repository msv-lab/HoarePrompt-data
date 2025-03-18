a = int(input())
for i in range(a):
    (x1, y1) = map(int, input().split())
    (x2, y2) = map(int, input().split())
    (x3, y3) = map(int, input().split())
    (x4, y4) = map(int, input().split())
    if x1 == x3 and x2 == x4:
        if y1 < y3:
            res = abs(y3 - y1)
        else:
            res = abs(y1 - y3)
    elif x1 == x2 and x3 == x4:
        if y1 < y2:
            res = abs(y2 - y1)
        else:
            res = abs(y1 - y2)
    elif x1 == x4 and x3 == x2:
        if y1 < y2:
            res = abs(y2 - y1)
        else:
            res = abs(y1 - y2)
    print(res ** 2)