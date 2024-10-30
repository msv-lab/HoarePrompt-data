t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    d = []
    h = []
    for _ in range(n):
        di, hi = map(int, input().split())
        d.append(di)
        h.append(hi)
    d.sort(reverse=True)
    h.sort()
    ans = 0
    for di, hi in zip(d, h):
        while x > 0:
            x -= min(di, x)
            if x > 0:
                x += hi
            ans += 1
            if x <= 0:
                break
        if x <= 0:
            break
    if x > 0:
        print(-1)
    else:
        print(ans)
