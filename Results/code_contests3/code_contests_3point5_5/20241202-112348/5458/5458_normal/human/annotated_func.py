#State of the program right berfore the function call: N, M, and S are positive integers such that 1 ≤ N ≤ 7, 1 ≤ M ≤ 2000, and 1 ≤ S ≤ 3000.**
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
        
    #State of the program after the loop has been executed: After all iterations of the loop have executed, the final values of `n`, `m`, `s`, `i`, `j+1`, `k` are integers between 1 and `m`. The 2D list `dp` with dimensions (`m + 2`) x (`s + 1`) is properly initialized. The final values of the elements in `dp` will be determined by the conditions met during the loop execution. If the loop does not execute, all variables will maintain their initial values.
#Overall this is what the function does:The function `func` reads inputs for `n`, `m`, and `s` until all three are zero. It then initializes a 2D list `dp` based on certain conditions and calculates values for this list. Finally, it prints a specific value from `dp`. The function operates within the constraints that `n`, `m`, and `s` are positive integers satisfying 1 ≤ N ≤ 7, 1 ≤ M ≤ 2000, and 1 ≤ S ≤ 3000. The function does not return any value.

