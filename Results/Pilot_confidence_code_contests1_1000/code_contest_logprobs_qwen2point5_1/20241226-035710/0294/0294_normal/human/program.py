

MOD = 1000000007

n, k = map(int, raw_input().split())
a = map(int, raw_input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    suma = 0
    l = 0
    r = 0
    for j in range(k + 1):
        if l < j - a[i - 1]:
            suma -= dp[i - 1][l]
            l += 1
        if r <= j:
            suma += dp[i - 1][r]
            r += 1
        suma %= MOD
        dp[i][j] += suma
        dp[i][j] %= MOD
print(dp[n][k])
