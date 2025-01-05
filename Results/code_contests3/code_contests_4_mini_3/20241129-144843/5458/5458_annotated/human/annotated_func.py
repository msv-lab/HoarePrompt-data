#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 7, M is a positive integer such that 1 ≤ M ≤ 2000, S is a positive integer such that 1 ≤ S ≤ 3000, and the input consists of multiple datasets ending with 0 0 0. Each dataset contains valid integers for N, M, and S.
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
        
    #State of the program after the loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 7; `n`, `m`, and `s` are non-negative integers where `n` and `m` are at least 0; `s` is at least 0; `dp` has been fully computed based on the defined conditions throughout the loop iterations; the output is `dp[N
#Overall this is what the function does:The function processes multiple datasets of three positive integers N, M, and S, where N is constrained between 1 and 7, M between 1 and 2000, and S between 1 and 3000. It calculates a specific value based on dynamic programming principles for each dataset, printing the result for each dataset until it encounters the terminating input of 0 0 0. The function handles the input directly and does not return a value in the traditional sense but instead prints results directly to the output.

