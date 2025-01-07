W = int(input())
cnt = list(map(int, input().split()))
dp = [0] * (W + 1)
for i in range(1, 9):
    for j in range(W, i - 1, -1):
        dp[j] = max(dp[j], dp[j - i] + i * cnt[i - 1])
print(dp[W])
