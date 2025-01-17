t = int(input())
for z in range(t):
    (n, m, k) = map(int, input().split())
    c = []
    for i in range(k):
        (x, y) = map(int, input().split())
        c.append((y, x, i))
    c.sort()
    f = [(1, 0, 0)]
    s = 0
    answer = [0] * k
    for i in range(k):
        if c[i][1] > f[-1][1]:
            s += (c[i][0] - 1) * (c[i][1] - f[-1][1])
            f.append((c[i][0], c[i][1], c[i][2]))
    answer[f[-1][2]] = 1
    for i in range(1, len(f) - 1):
        if f[i][0] < f[i + 1][0]:
            answer[f[i][2]] = 1
    print(s + (n - f[-1][1]) * m)
    print(*answer)