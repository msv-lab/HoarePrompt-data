t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    s = 0
    m = 1
    while n:
        x = (n + 1) // 2
        n //= 2
        if s < k and k <= s + x:
            break
        s += x
        m *= 2
    print((2 * (k - s) - 1) * m)