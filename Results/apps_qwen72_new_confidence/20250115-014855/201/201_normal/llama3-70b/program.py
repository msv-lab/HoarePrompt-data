h1, h2 = map(int, input().split())
a, b = map(int, input().split())

if a <= b:
    print(-1)
else:
    days = 0
    while h1 < h2:
        h1 += a
        days += 1
        if h1 >= h2:
            break
        h1 -= b
    print(days)
