#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 7, M is a positive integer such that 1 ≤ M ≤ 2000, S is a positive integer such that 1 ≤ S ≤ 3000. The input consists of multiple datasets ending with a line containing "0 0 0". The number of datasets does not exceed 5.
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
        
    #State of the program after the loop has been executed: `n` is a positive integer, `m` is a positive integer, `s` is a positive integer, the final value of `dp` reflects the results of the calculations performed in the nested loops for all values of `j` from 1 to `m` and `k` from 1 to `s`; the printed output is `dp[n^2 & 1][m + 1][s] % mod`
#Overall this is what the function does:The function reads multiple datasets consisting of three positive integers (N, M, S) until it encounters the line "0 0 0". For each dataset, it calculates a value based on a dynamic programming approach and prints the result. The function handles datasets with constraints on N (1 to 7), M (1 to 2000), and S (1 to 3000), and it outputs the computed value modulo 100000 for each dataset. The function does not return any values; it only prints the results.

