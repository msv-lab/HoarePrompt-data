def func_1(n, m, k, a, b):
    cb = Counter(sorted(b))
    ca = Counter(sorted(a[:m]))
    ans = 0
    sm = sum((ca & cb).values())
    if sm >= k:
        ans += 1
    for r in range(m, n):
        if ca[a[r]] < cb[a[r]]:
            sm += 1
        ca[a[r]] += 1
        if ca[a[r - m]] <= cb[a[r - m]]:
            sm -= 1
        ca[a[r - m]] -= 1
        if sm >= k:
            ans += 1
    return ans
for _ in range(int(input())):
    (n, m, k) = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(func_1(n, m, k, a, b))