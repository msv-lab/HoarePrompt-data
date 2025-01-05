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
        
    #State of the program after the loop has been executed: After the loop executes, the variables `dp`, `n`, `m`, `s`, `j`, `k`, `i` will be integers with their initial conditions. The final values of `dp` will be correctly updated based on the conditions specified in the loop code. The values of `dp` will be determined by the calculations within the loop, considering the initial conditions of `n`, `m`, `s`, `j`, `k`, `i`. If the loop does not execute at all, then the final values of the variables will remain the same as their initial values.
#Overall this is what the function does:The function `func` reads input until it encounters a case where `n`, `m`, and `s` are all 0, at which point it breaks out of the loop. Within the loop, the function performs a series of calculations on the variables `dp`, `n`, `m`, and `s` based on the nested loops and conditions specified. The final output printed is the result of the calculations done on `dp[n

