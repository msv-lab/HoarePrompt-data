#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 7, M is a positive integer such that 1 ≤ M ≤ 2000, S is a positive integer such that 1 ≤ S ≤ 3000. The input consists of multiple datasets, and ends when N, M, S are all 0. The number of datasets does not exceed 5.
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
        
    #State of the program after the loop has been executed: `n` is a positive integer, `m` is a positive integer, `s` is a positive integer, `dp` is a 2D array reflecting the combinations of selections based on all iterations from `1` to `m` and from `1` to `s`, the output is `dp[n
#Overall this is what the function does:The function processes multiple datasets consisting of three positive integers N, M, and S, where 1 ≤ N ≤ 7, 1 ≤ M ≤ 2000, and 1 ≤ S ≤ 3000. It continues processing until N, M, and S are all zero. The function calculates a value based on dynamic programming using a 2D array to reflect combinations of selections and prints the result for each dataset. The function does not take any parameters and does not handle cases where N, M, or S exceed their specified limits during execution.

