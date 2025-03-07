for _ in range(int(input())):
    (n, m) = map(int, input().split())
    l = list(map(int, input().split()))
    p = [0]
    c = [0]
    (i, j) = (0, 0)
    for x in l:
        if x == 1:
            j += 1
        i += x
        p.append(i)
        c.append(j)
    for _ in range(m):
        (a, b) = map(int, input().split())
        i = c[b] - c[a - 1]
        s = p[b] - p[a - 1]
        if b - a + 1 > 1 and s - (b - a + 1) >= i:
            print('YES')
        else:
            print('NO')