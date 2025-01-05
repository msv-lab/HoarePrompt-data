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
        
    #State of the program after the loop has been executed: The final state of the variables (N, M, S, mod, i, j, k) will be determined by the logic of the loop and the conditions met during each iteration. The value printed is dp[n] % mod. The values of `n`, `m`, `s`, `k`, and `i` will remain unchanged, while the value of `j` will be equal to `m + 1`
#Overall this is what the function does:The function `func` does not accept any parameters. It operates with predefined positive integers N, M, and S where 1 ≤ N ≤ 7, 1 ≤ M ≤ 2000, and 1 ≤ S ≤ 3000. The function reads input from the user until N, M, and S are all 0. It then performs a series of calculations using dynamic programming techniques and finally prints a result based on the values of N, M, and S.

