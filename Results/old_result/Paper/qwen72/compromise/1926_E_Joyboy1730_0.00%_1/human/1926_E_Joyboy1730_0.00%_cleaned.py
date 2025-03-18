t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    L = []
    while n:
        m = (n + 1) // 2
        n -= m
    tot = 0
    pow = 1
    for a in L:
        if tot < k and k <= tot + a:
            print(pow * (2 * k - 1))
            break
        tot += a
        k -= tot
        pow *= 2