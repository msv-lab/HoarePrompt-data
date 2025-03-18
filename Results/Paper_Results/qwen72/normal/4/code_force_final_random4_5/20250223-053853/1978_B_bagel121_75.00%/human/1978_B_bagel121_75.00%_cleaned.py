t = int(input())
for _ in range(t):
    (n, a, b) = map(int, input().split())
    if a >= b:
        print(n * a)
    else:
        k = min(b - a + 1, n)
        ans = int((b + (b - k + 1)) / 2 * k)
        p2 = (n - k) * a
        print(ans + p2)