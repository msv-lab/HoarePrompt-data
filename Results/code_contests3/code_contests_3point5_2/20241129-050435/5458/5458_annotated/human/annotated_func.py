#State of the program right berfore the function call: N, M, S are positive integers such that 1 ≤ N ≤ 7, 1 ≤ M ≤ 2000, and 1 ≤ S ≤ 3000.**
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
        
    #State of the program after the loop has been executed: `dp` is a 3D list with updated values based on the conditions in the loop for all possible combinations of `i`, `j`, and `k`. The loop control variables `n`, `m`, `s` are all 0, and the code snippet prints the modulo of the value at `dp[0][1][0]`
#Overall this is what the function does:The function `func` reads input for positive integers N, M, and S. It then performs calculations using a dynamic programming approach to update a 3D list `dp` based on certain conditions within nested loops. Finally, it prints the modulo of a specific value from `dp`. The function continues this process until N, M, and S are all 0. The function does not have specific return values and operates within the constraints of the provided positive integer limits.

