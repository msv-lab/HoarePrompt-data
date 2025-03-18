n, k, M = map(int, input().split())
t = list(map(int, input().split()))
t.sort()
dp = [[0] * (M + 1) for _ in range(k + 1)]
for i in range(1, k + 1):
    for j in range(1, M + 1):
        dp[i][j] = dp[i][j - 1]
        if j >= t[i - 1]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - t[i - 1]] + 1)
print(sum(dp[i][M] for i in range(k + 1)) + sum(1 for i in range(k + 1) if dp[i][M] == i))
