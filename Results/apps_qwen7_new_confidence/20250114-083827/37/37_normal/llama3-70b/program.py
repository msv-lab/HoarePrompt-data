n = int(input())
if n == 0:
    print(0, 0)
else:
    m = 1
    while True:
        if (m * (m - 1)) // 2 >= n:
            break
        m += 1
    x, y = 0, 0
    if m % 2 == 1:
        dx, dy = 1, 0
    else:
        dx, dy = 0, -1
    for _ in range((m - 1) * (m - 2) // 2, (m - 1) * (m - 2) // 2 + n - 1):
        x += dx
        y += dy
        if _ % (m - 1) == 0:
            if m % 2 == 1:
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx
    print(x, y)
