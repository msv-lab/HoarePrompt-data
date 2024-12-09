(m, a, b) = map(int, input().split())
dp = [0] * (m + 1)
dp[0] = 1
for i in range(m + 1):
    if i + a <= m:
        dp[i + a] += dp[i]
    if i - b >= 0:
        dp[i] += dp[i - b]
print(sum(dp))