#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 7, M is a positive integer such that 1 ≤ M ≤ 2000, S is a positive integer such that 1 ≤ S ≤ 3000, and input ends when N, M, S are all 0.
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
        
    #State of the program after the loop has been executed: `n` is 0, `m` is 0, `s` is 0; `dp` is a 2D list with dimensions (2, M + 2) containing computed values based on the dynamic programming logic; the last printed value is `dp[n^2 & 1][m + 1][s] % mod`.
#Overall this is what the function does:The function reads multiple sets of positive integers N, M, and S until all three are zero. It computes a value based on a dynamic programming approach using these inputs and outputs the result for each valid set of inputs. The function ensures that the computed value is taken modulo 100000 before printing. The exact nature of the computation involves filling a 2D list based on conditions involving the input values, but the overall logic and purpose of the computation are not explicitly detailed in the annotations.

