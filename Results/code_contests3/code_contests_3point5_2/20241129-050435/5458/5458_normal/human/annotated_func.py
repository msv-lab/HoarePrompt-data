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
        
    #State of the program after the loop has been executed: After all iterations of the loop have finished, the final values of `n`, `m`, `s`, `i`, `j`, `k`, and `dp[(i + 1) & 1][j + 1][s + 1]` cannot be accurately determined due to the complex conditional statements within the loop code. The values are dependent on the initial state of the variables and the specific conditions met during each iteration. If the loop does not execute, the values of the variables will remain the same as the initial state.
#Overall this is what the function does:The function `func` does not accept any parameters. It operates with predefined positive integer variables N, M, and S, where 1 ≤ N ≤ 7, 1 ≤ M ≤ 2000, and 1 ≤ S ≤ 3000. The function reads input values for n, m, and s until all three are 0. It then performs a complex calculation using dynamic programming to update a 3D array `dp`. The final result is printed based on specific indices of the `dp` array. The function does not have a specific return value specified, as the output is dependent on the operations performed within the function body. The loop continues until n, m, and s are all 0.

