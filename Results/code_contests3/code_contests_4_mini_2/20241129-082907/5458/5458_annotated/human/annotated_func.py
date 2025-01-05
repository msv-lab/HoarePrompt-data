#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 7, M is a positive integer such that 1 ≤ M ≤ 2000, S is a positive integer such that 1 ≤ S ≤ 3000. The input consists of multiple datasets, each containing N, M, and S, and ends with a dataset of "0 0 0". The number of datasets does not exceed 5.
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
        
    #State of the program after the loop has been executed: `n` is 0, `m` is the last positive integer input value, `s` is the last positive integer input value, `dp` is a fully computed 2D list with the results from all iterations of the nested loops, and the final printed value is `dp[n
#Overall this is what the function does:The function reads multiple datasets of positive integers N, M, and S, where 1 ≤ N ≤ 7, 1 ≤ M ≤ 2000, and 1 ≤ S ≤ 3000. For each dataset, it performs computations based on nested loops to fill a 2D list `dp` and prints the value of `dp[n^2 & 1][m + 1][s] % mod`. The function continues processing until it encounters the dataset "0 0 0", which signals it to stop. The output is the computed result for each dataset based on the dynamic programming approach implemented in the nested loops.

