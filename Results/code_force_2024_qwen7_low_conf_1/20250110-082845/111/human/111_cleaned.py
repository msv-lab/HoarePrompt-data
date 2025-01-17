MOD = 998244353

def func_1(n, k):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    dp[1][1] = 1
    for i in range(2, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % MOD
    result = sum((dp[i][n] for i in range(1, k + 1))) % MOD
    return result
t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    print(func_1(n, k))