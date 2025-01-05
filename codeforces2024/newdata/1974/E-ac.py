t = int(input())
for _ in range(t):
    m, x = map(int, input().split())
    l = [tuple(map(int, input().split())) for _ in range(m)]
    s = sum(j for _, j in l)
    dp = [float('inf')] * (s + 1)
    dp[0] = 0
    for i in range(m):
        c, h = l[i]
        for k in range(s, h - 1, -1):
            if dp[k - h] + c <= i * x:
                dp[k] = min(dp[k], dp[k - h] + c)

    for k in range(s, -1, -1):
        if dp[k] != float('inf'):
            print(k)
            break
    else:
        print(0)