def func_1(a, p, s, k):
    n = len(p)
    mx = 0
    cur = 0
    vis = [0 for _ in range(n)]
    while not vis[s] and k > 0:
        vis[s] = 1
        mx = max(mx, cur + k * a[s])
        cur += a[s]
        k -= 1
        s = p[s]
    return mx
for _ in range(int(input())):
    (n, k, pb, ps) = map(int, input().split())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    for i in range(n):
        p[i] -= 1
        a[i] -= 1
    A = func_1(a, p, pb - 1, k)
    B = func_1(a, p, ps - 1, k)
    if A == B:
        print('Draw')
    elif A > B:
        print('Bodya')
    else:
        print('Sasha')