n = int(input())
cakes = []
for _ in range(n):
    (r, h) = map(int, input().split())
    cakes.append((math.pi * r * r * h, r, h))
cakes.sort(reverse=True)
dp = [0.0] * n
dp[0] = cakes[0][0]
for i in range(1, n):
    dp[i] = cakes[i][0]
    for j in range(i):
        if cakes[i][1] < cakes[j][1] and cakes[i][2] < cakes[j][2]:
            dp[i] = max(dp[i], dp[j] + cakes[i][0])
print(dp[-1])