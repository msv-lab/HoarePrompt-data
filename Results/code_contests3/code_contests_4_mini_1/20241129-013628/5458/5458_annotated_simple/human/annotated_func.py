#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 7, M is a positive integer such that 1 ≤ M ≤ 2000, S is a positive integer such that 1 ≤ S ≤ 3000, and the input consists of multiple datasets ending with '0 0 0'. Each dataset contains three integers N, M, S separated by spaces. The number of datasets does not exceed 5.
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
        
    #State of the program after the loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 7; `n` is equal to `N`; `m` is a positive integer such that 1 ≤ `M` ≤ 2000; `s` is a positive integer such that 1 ≤ `S` ≤ 3000; `i` is equal to `N^2`; `dp` contains the computed values based on the conditions applied throughout all iterations; the result printed is `dp[N^2 & 1][M + 1][S] % mod`.
#Overall this is what the function does:The function accepts multiple datasets where each dataset contains three positive integers N (1 ≤ N ≤ 7), M (1 ≤ M ≤ 2000), and S (1 ≤ S ≤ 3000). It processes these datasets in a loop and computes a result based on dynamic programming principles until the dataset '0 0 0' is encountered. The computed result for each dataset is printed, specifically the value at `dp[N^2 & 1][M + 1][S] % 100000`. The function does not return any values but outputs results for each dataset processed.

