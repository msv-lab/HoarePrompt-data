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
        
    #State of the program after the loop has been executed: At the end of the loop execution, the final values of `dp` at various indices will be updated with mapped integer values based on the conditions within the loop. `n` will be updated to the next value after the loop finishes, `m` will remain greater than 0, `s` will be at least 1. `j` will range from 1 to `m`, and `k` will range from 1 to `s`.
#Overall this is what the function does:The function `func` reads input values for `n`, `m`, and `s` until all three are 0. It then performs a series of calculations using dynamic programming to update values in a multidimensional array `dp`. The final result is printed based on the updated values in `dp`. The function does not have a specific return value and operates within the constraints provided for `n`, `m`, and `s`.

