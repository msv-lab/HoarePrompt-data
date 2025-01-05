

MOD = 1000000007

n = input()
a = []
for _ in range(n):
    a.append(map(int, raw_input().split()))

dp = [[0] * (1 << n) for _ in range(n + 1)]
for i in range(1 << n):
    dp[0][i] = 1
for i in range(1, n + 1):
    for mask in range(1, 1 << n):
        for j in range(n):
            if a[i - 1][j] == 1 and mask & (1 << j):
                dp[i][mask] += dp[i - 1][mask ^ (1 << j)]
                dp[i][mask] %= MOD
print(dp[n][(1 << n) - 1])