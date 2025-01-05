#State of the program right berfore the function call: N is an integer between 1 and 7 inclusive, M is an integer between 1 and 2000 inclusive, S is an integer between 1 and 3000 inclusive. The input ends when N, M, S are all zero. The number of datasets does not exceed 5.
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
        
    #State of the program after the loop has been executed: `n` is a positive integer between 1 and 7, `m` is an integer between 1 and 2000, `s` is an integer between 1 and 3000, `i` is `n^2`, `j` is `m + 1`, `k` is `s + 1`, and `dp` contains the computed values based on the last inputs of `n`, `m`, and `s`; the printed output is `dp[n^2 & 1][m + 1][s] % mod`.
#Overall this is what the function does:The function processes up to 5 datasets of integers N, M, and S, where N is between 1 and 7 inclusive, M is between 1 and 2000 inclusive, and S is between 1 and 3000 inclusive. For each dataset, it computes and prints a value based on a dynamic programming approach using a 3D array, with the result being `dp[n^2 & 1][m + 1][s] % 100000`. The function terminates when N, M, and S are all zero.

