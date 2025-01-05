#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 7, M is a positive integer such that 1 ≤ M ≤ 2000, and S is a positive integer such that 1 ≤ S ≤ 3000. The input ends when N, M, S are all zero. The number of datasets does not exceed 5.
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
        
    #State of the program after the loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 7; `n` is 0; `m` is the final input value of `m`; `s` is the final input value of `s`; `dp` is fully updated with the results from all iterations; the output is `dp[N^2 & 1][m + 1][s] % 100000`.
#Overall this is what the function does:The function processes multiple datasets defined by positive integers N, M, and S, where N is between 1 and 7, M is between 1 and 2000, and S is between 1 and 3000, terminating when all inputs are zero. For each dataset, the function calculates a value using a dynamic programming approach and outputs the result of the computation `dp[N^2 & 1][M + 1][S] % 100000` for each valid input set. The function does not define the output specifics beyond this computational result.

