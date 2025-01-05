#State of the program right berfore the function call: N is a positive integer, and a_{i, j} is either 0 or 1 for 1 <= i, j <= N.**
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: N is a positive integer, a_{i, j} is either 0 or 1 for 1 <= i, j <= N, MOD is 1000000007, a contains the mapped integer values from all input iterations
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: dp[0][i] is assigned the value 1 for all values of i in the range (1 << N)
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: All `dp[i][mask]` values have been correctly updated for all valid `i`, `mask`, and `j` values within the loop. The values of `dp[i][mask]` have been computed based on the conditions specified in the loop code for each valid `j` value. `n` is greater than or equal to 1, `mask` is `(1 << n) - 1`, `i` is `n`. The remainder operation with `MOD` has been applied to all updated `dp[i][mask]` values.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function `func` reads an integer `n` from input and populates a matrix `a` of size N x N with integer values. It then performs a series of calculations on a dynamic programming table `dp` based on the values in matrix `a` and prints the final result. The function does not accept any parameters and its main functionality revolves around matrix manipulations and dynamic programming operations.

