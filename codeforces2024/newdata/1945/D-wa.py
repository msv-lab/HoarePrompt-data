t = int(input().strip())
for _ in range(t):
    n, m = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    res = 0
    for i in reversed(range(m, n)):
        res += min(a[i], b[i])
    res += a[m - 1]
    print(res)
