def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if w == w // 1 and w >= x - 1:
        M += [w]
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        i += 1
    return M
t = int(input())
for _ in range(t):
    L = list(map(int, input().split()))
    n = L[0]
    x = L[1]
    ans = 0
    y = n + x
    if y % 2 != 0:
        print(0)
        continue
    else:
        L1 = func_1((y - 2) // 2, x)
        if n >= 3 * x - 2:
            L1 += func_1((n - x) // 2, x)
        L1 = list(set(L1))
        print(len(L1))
        continue