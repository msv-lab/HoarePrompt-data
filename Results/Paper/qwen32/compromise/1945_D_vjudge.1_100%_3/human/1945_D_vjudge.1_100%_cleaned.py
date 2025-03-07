def func_1(n, k, a, b):
    c = [min(a[i], b[i]) for i in range(n)]
    suff = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suff[i] = suff[i + 1] + c[i]
    ans = float('inf')
    for i in range(k):
        ans = min(ans, a[i] + suff[i + 1])
    print(ans)
t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    func_1(n, k, a, b)