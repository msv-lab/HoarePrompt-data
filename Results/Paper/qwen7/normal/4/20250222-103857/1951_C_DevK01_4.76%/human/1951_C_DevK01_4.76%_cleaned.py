t = int(input())
for _ in range(t):
    L = list(map(int, input().split()))
    M = list(map(int, input().split()))
    (n, m, k) = (L[0], L[1], L[2])
    m = min(m, k)
    M.sort()
    q = int(math.ceil(k / m))
    N = M[:q]
    n = len(N)
    if n * m == k:
        cost = m * sum(N) + m * m * ((n - 1) * n // 2)
    else:
        w = N.pop()
        mu = k - (n - 1) * m
        cost = mu * w
        n = len(N)
        cost += m * sum(N) + m * m * ((n - 1) * (n - 2) // 2) + n * m * mu
    print(cost)
    continue