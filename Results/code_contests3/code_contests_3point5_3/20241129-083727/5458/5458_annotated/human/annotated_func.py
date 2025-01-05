#State of the program right berfore the function call: **
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
        
    #State of the program after the loop has been executed: At the end of the loop, the values of `n`, `m`, `s`, `i`, `j`, `k` are integers, and the `dp` array is fully updated based on the loop conditions. The final value printed is the modulo of the value in the `dp` array at the calculated index.
#Overall this is what the function does:The function reads input from the user until the values of `n`, `m`, and `s` are all zero. For each set of non-zero inputs, it performs calculations on the `dp` array, and at the end of each iteration, it prints the modulo of a specific value from the `dp` array. The function does not accept any parameters and does not return any value.

