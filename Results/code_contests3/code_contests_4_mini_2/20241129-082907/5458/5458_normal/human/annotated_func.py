#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 7, M is a positive integer such that 1 ≤ M ≤ 2000, S is a positive integer such that 1 ≤ S ≤ 3000, and the input terminates when N, M, S are all 0. The number of datasets does not exceed 5.
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
        
    #State of the program after the loop has been executed: `N`, `M`, `S` are the input values; `dp` contains values computed from the nested loops based on the input conditions; `i` is equal to `N^2`; the final output is `dp[N^2 & 1][M + 1][S] % mod`, and the loop stops executing when `n`, `m`, `s` are all 0 after the last input.
#Overall this is what the function does:The function processes multiple datasets of three positive integers N, M, and S, where N ranges from 1 to 7, M ranges from 1 to 2000, and S ranges from 1 to 3000. It calculates and prints a value derived from a dynamic programming table based on these inputs. The processing terminates when all three inputs are 0. The function handles up to 5 datasets and outputs the computed result for each dataset.

