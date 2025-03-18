def count_trees(n):
    MOD = 998244353
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1] * ((i - 1) // j % 2)
            dp[i] %= MOD
    return dp[n]

n = int(input())
print(count_trees(n))
