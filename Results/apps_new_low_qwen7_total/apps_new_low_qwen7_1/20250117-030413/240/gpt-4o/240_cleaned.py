def func_1(n, m):
    if n >= 2 and m >= 2:
        points = [(0, 0), (n, 0), (n, m), (0, m)]
    elif n == 0:
        points = [(0, 0), (0, m), (0, 1), (0, m - 1)]
    elif m == 0:
        points = [(0, 0), (n, 0), (1, 0), (n - 1, 0)]
    elif n == 1:
        points = [(0, 0), (1, 0), (1, m), (0, m)]
    else:
        points = [(0, 0), (0, 1), (n, 1), (n, 0)]
    return points
(n, m) = map(int, input().split())
result = func_1(n, m)
for point in result:
    print(point[0], point[1])