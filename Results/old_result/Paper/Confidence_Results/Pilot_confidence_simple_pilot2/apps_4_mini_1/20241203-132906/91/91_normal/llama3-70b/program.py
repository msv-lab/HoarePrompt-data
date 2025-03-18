import math

n, k, S = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0]*(k+1) for _ in range(S+1)]
dp[0][0] = 1

for i in range(1, S+1):
    for j in range(k+1):
        dp[i][j] = dp[i][j]
        for x in range(n):
            if i >= a[x] and j >= 1:
                dp[i][j] += dp[i-a[x]][j-1]
            if i >= math.factorial(a[x]) and j >= 1:
                dp[i][j] += dp[i-math.factorial(a[x])][j-1]

print(dp[S][k])
