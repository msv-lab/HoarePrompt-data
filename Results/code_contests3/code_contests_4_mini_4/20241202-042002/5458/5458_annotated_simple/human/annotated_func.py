#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 7, M is a positive integer such that 1 ≤ M ≤ 2000, S is a positive integer such that 1 ≤ S ≤ 3000. The input consists of multiple datasets, and ends when N, M, S are all 0. The number of datasets does not exceed 5.
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
        
    #State of the program after the loop has been executed: `N` is an integer such that 1 ≤ `N` ≤ 7; `n` is 0, `m` is 0, `s` is 0; `dp` contains the computed values based on the last set of inputs before exiting the loop; the last printed output is the final value obtained from `dp[N^2 & 1][m + 1][s] % mod`
#Overall this is what the function does:The function processes multiple datasets of integers N, M, and S, where N is constrained between 1 and 7, M is a positive integer up to 2000, and S is a positive integer up to 3000. It continues processing until a dataset with N, M, and S all equal to 0 is encountered. For each valid dataset, it performs a dynamic programming calculation and prints the result derived from a 3D list `dp`, which represents computed values based on the input. The function does not return any values; instead, it outputs results directly to the console.

