for _ in range(int(input())):
    (n, m) = map(int, input().split())
    l = list(map(int, input().split()))
    p = []
    c = 0
    for x in l:
        c += x
        p.append(c)
    for _ in range(m):
        (a, b) = map(int, input().split())
        s = p[b - 1]
        if a - 2 >= 0:
            s -= p[a - 2]
        if b - a + 1 > 1 and s >= 2 * (b - a + 1):
            print('YES')
        else:
            print('NO')