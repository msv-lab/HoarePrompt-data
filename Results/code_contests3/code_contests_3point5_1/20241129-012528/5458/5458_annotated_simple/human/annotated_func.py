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
        
    #State of the program after the loop has been executed: After the loop executes, the values of N, M, S, mod, n, m, s, i, j, k will remain positive integers meeting the given constraints. The dp array will be updated based on the conditions within the loop, with the final values dependent on the specific values of N, M, S, mod, n, m, s, j, k and the conditions specified in the loop.
#Overall this is what the function does:The function `func` reads input values for N, M, and S from the user within a while loop. It then initializes a dynamic programming array `dp` and updates its values based on nested loops and specific conditions. The final result is printed after the loop exits. The function does not accept any parameters and does not explicitly return a value.

