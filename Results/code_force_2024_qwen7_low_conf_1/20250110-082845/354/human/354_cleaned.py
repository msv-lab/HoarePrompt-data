def func_1(c1, c2, c3, c4):
    MOD = 998244353
    dp = [[0 for _ in range(4)] for _ in range(max(c1, c2, c3, c4) + 1)]
    dp[0][0] = 1
    for i in range(1, max(c1, c2, c3, c4) + 1):
        if i <= c1:
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]) % MOD
        if i <= c2:
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2] + dp[i - 1][3]) % MOD
        if i <= c3:
            dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][3]) % MOD
        if i <= c4:
            dp[i][3] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD
    total_ways = sum(dp[max(c1, c2, c3, c4)]) % MOD
    return total_ways

def func_2():
    MOD = 998244353
    t = int(input())
    results = []
    for _ in range(t):
        (c1, c2, c3, c4) = map(int, input().split())
        result = func_1(c1, c2, c3, c4)
        results.append(result)
    for result in results:
        print(result)
if __name__ == '__main__':
    func_2()