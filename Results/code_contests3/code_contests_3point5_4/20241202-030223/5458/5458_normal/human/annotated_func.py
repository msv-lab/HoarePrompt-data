#State of the program right berfore the function call: N, M, and S are positive integers such that 1 <= N <= 7, 1 <= M <= 2000, and 1 <= S <= 3000.**
def func():
    mod = 100000
    while 1:
        n, m, s = map(int, raw_input().split())
        
        if n == m == s == 0:
            break
        
        dp = [[([0] * (s + 1)) for _ in xrange(m + 2)] for _ in xrange(2)]
        
        for i in xrange(n ** 2):
            for j in xrange(1, m + 1):
                for k in xrange(1, s + 1):
                    if i == 0:
                        if j >= k:
                            dp[i + 1 & 1][j + 1][k] = 1
                    else:
                        if j > k:
                            dp[i + 1 & 1][j + 1][k] = dp[i + 1 & 1][j][k]
                            continue
                        dp[i + 1 & 1][j + 1][k] = dp[i + 1 & 1][j][k] % mod
                        dp[i + 1 & 1][j + 1][k] += dp[i & 1][j][k - j] % mod
        
        print(dp[n ** 2 & 1][m + 1][s] % mod)
        
    #State of the program after the loop has been executed: After all iterations of the loop have finished, the final calculated value of dp[n] is stored in the variable dp[n
#Overall this is what the function does:The function `func` reads input values for N, M, and S within specific constraints. It then performs calculations using dynamic programming to fill a 3D array `dp` and outputs a specific value based on these calculations. The function continues this process until N, M, and S are all equal to 0.

