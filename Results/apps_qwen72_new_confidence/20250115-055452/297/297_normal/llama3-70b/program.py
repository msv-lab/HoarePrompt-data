n = int(input())
a, b = map(int, input().split())
h = list(map(int, input().split()))

dp = [[float('inf')] * (a + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(a + 1):
        if j >= h[i - 1]:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - h[i - 1]] + (h[i - 1] if i > 1 and h[i - 1] != h[i - 2] else 0))
        dp[i][j] = min(dp[i][j], dp[i - 1][j])

ans = float('inf')
for i in range(a, -1, -1):
    if dp[n][i] != float('inf'):
        ans = min(ans, dp[n][i])

if ans == float('inf') or a + b < sum(h):
    print(-1)
else:
    print(ans)
