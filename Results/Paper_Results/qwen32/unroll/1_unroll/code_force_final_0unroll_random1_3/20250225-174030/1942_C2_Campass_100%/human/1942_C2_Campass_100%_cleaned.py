R = lambda : map(int, input().split())
(t,) = R()
while t:
    t -= 1
    (n, x, y) = R()
    sx = 0
    l = list(R())
    l.sort()
    l.append(n + l[0])
    val = []
    for i in range(1, x + 1):
        c = l[i] - l[i - 1] - 1
        val.append(c)
    val.sort(key=lambda x: (1 - x & 1, x))
    for i in val:
        c = i // 2
        if y < c:
            sx += y * 2
            break
        sx += i
        y -= c
    cons = x + sx - 2
    print(cons)