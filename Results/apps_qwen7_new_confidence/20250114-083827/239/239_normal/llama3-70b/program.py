n, m, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * (n + 1)
mx = 0

for i in range(1, n + 1):
    dp[i] = max(dp[i - 1], sum(a[:i]) - k * ((i + m - 1) // m))
    mx = max(mx, dp[i])

print(mx)
