#State of the program right berfore the function call: N, M, S are positive integers such that 1 <= N <= 7, 1 <= M <= 2000, and 1 <= S <= 3000.**
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
        
    #State of the program after the loop has been executed: The final values of `N`, `M`, `S`, `mod`, `n`, `m`, `s`, and `dp` will be determined based on the conditions in the loop code. The `dp` matrix will hold the calculated values based on the conditions specified in the loop code. The value printed is `dp[n`. All variables will be integers within their specified ranges, and the loop control variables will have their final values after the loop execution.
#Overall this is what the function does:The function `func` reads input until the values of `n`, `m`, and `s` are all 0, then it calculates values based on the constraints provided in the loop. It utilizes dynamic programming to populate a matrix `dp` with calculated values. The final output is the result obtained from the `dp` matrix. The function does not explicitly return any value but prints the result.

