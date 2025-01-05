#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 7, M is a positive integer such that 1 ≤ M ≤ 2000, and S is a positive integer such that 1 ≤ S ≤ 3000. The input consists of multiple datasets, and the termination condition is indicated by N, M, S being 0.
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
        
    #State of the program after the loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 7; `i` is `N^2`; `M` is a positive integer such that 1 ≤ `M` ≤ 2000; `S` is a positive integer such that 1 ≤ `S` ≤ 3000; the output is `dp[N^2 & 1][M + 1][S] % mod`; the loop continues until the input values of `n`, `m`, and `s` are all zero.
#Overall this is what the function does:The function processes multiple datasets consisting of three integers N, M, and S. It calculates a specific dynamic programming value based on these integers and prints the result for each dataset. The function continues to process datasets until all three integers are zero, at which point it terminates. The expected ranges for N, M, and S are 1 ≤ N ≤ 7, 1 ≤ M ≤ 2000, and 1 ≤ S ≤ 3000. The outputs are computed using a dynamic programming table, and results are taken modulo 100000. The function does not return any values; rather, it prints the results directly.

