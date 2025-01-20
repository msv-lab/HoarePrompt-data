(x1, y1, x2, y2) = map(int, input().split())
if x1 == x2:
    (x3, x4) = (x1 + abs(y1 - y2), x1 - abs(y1 - y2))
    (y3, y4) = (y1, y2)
else:
    (y3, y4) = (y1 + abs(x1 - x2), y1 - abs(x1 - x2))
    (x3, x4) = (x1, x2)
if -1000 <= x3 <= 1000 and -1000 <= x4 <= 1000 and (-1000 <= y3 <= 1000) and (-1000 <= y4 <= 1000):
    print(x3, y3, x4, y4)
else:
    print(-1)