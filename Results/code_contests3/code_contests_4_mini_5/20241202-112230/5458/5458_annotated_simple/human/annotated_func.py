#State of the program right berfore the function call: N is a positive integer (1 ≤ N ≤ 7), M is a positive integer (1 ≤ M ≤ 2000), S is a positive integer (1 ≤ S ≤ 3000), and there are multiple datasets provided until a dataset with N, M, S as 0 is encountered. The number of datasets does not exceed 5.
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
        
    #State of the program after the loop has been executed: `N` is a positive integer (1 ≤ N ≤ 7), `M` is a positive integer (1 ≤ M ≤ 2000), `S` is a positive integer (1 ≤ S ≤ 3000), `dp` has been fully populated based on the inputs, and the final printed value is `dp[N^2 & 1][M + 1][S] % 100000`.
#Overall this is what the function does:The function processes multiple datasets of positive integers N (1 ≤ N ≤ 7), M (1 ≤ M ≤ 2000), and S (1 ≤ S ≤ 3000), and for each dataset, it calculates a value stored in a dynamic programming table based on the inputs, printing the result modulo 100000. The function continues to process datasets until it encounters a dataset with N, M, and S all equal to 0, at which point it stops execution. The output behavior is specified as printing the computed value for each dataset.

