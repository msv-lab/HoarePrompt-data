#State of the program right berfore the function call: N is a positive integer (1 ≤ N ≤ 7), M is a positive integer (1 ≤ M ≤ 2000), S is a positive integer (1 ≤ S ≤ 3000), and the input consists of multiple datasets ending with "0 0 0". Each dataset contains three integers separated by spaces.
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
        
    #State of the program after the loop has been executed: `N` is a positive integer, `M` is a positive integer, `S` is a positive integer, the loop has completed execution for all input values until `n`, `m`, and `s` are all 0, `dp` contains the computed values based on the conditions of the loop, and the last output is `dp[N^2 & 1][M + 1][S] % mod`.
#Overall this is what the function does:The function processes multiple datasets of three positive integers N, M, and S, where N ranges from 1 to 7, M from 1 to 2000, and S from 1 to 3000. It continues processing datasets until the input "0 0 0" is encountered. For each dataset, it computes a value based on a dynamic programming approach and prints the result, which is derived from a 3D list `dp`. The final printed result for each dataset is `dp[N^2 & 1][M + 1][S] % 100000`. The function does not handle cases where the input does not fall within the specified ranges or if the input is malformed, as it relies on valid input as per the constraints mentioned.

