#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 7, M is a positive integer such that 1 ≤ M ≤ 2000, S is a positive integer such that 1 ≤ S ≤ 3000, and the input ends when N, M, S are all zero. Each dataset is valid, and the number of datasets does not exceed 5.
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
        
    #State of the program after the loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 7; `i` is `N^2`; `j` is `M + 1`; `k` is `S + 1`; `dp` has been fully updated based on all iterations for all values from 1 to `M` and 1 to `S`; the output is `dp[N^2 & 1][M + 1][S] % mod`, and the loop terminates when `n`, `m`, `s` are all 0.
#Overall this is what the function does:The function processes multiple datasets of positive integers `N`, `M`, and `S`, where the input ends when all three values are zero. For each dataset, it computes a value based on a dynamic programming approach using the parameters `N`, `M`, and `S`, and prints the result modulo 100,000. The function does not accept parameters directly and can handle up to 5 datasets. If the input values exceed their specified ranges or if the input consists solely of zeros, it terminates the process without further action.

