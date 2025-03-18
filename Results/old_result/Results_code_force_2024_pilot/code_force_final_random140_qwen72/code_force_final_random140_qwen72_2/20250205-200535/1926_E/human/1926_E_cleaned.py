for _ in range(int(input())):
    (n, k) = map(int, input().split())
    s = 0
    i = 0
    d = n
    h = n
    p = 1
    g = 0
    if k > (n + 1) // 2:
        while s < k and d > 0:
            s += (d + 1) // 2
            d -= (d + 1) // 2
            i += 1
        while p <= i - 1:
            g += (h + 1) // 2
            h -= (h + 1) // 2
            p += 1
        f = k - g
        y = 2 ** (i - 1) * f
        print(y)
    else:
        print(2 * k - 1)