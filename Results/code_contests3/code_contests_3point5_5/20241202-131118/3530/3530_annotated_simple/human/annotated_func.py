#State of the program right berfore the function call: ** N is a positive integer. The values of a_{i,j} are either 0 or 1.
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: N is a positive integer, the values of a_{i,j} are either 0 or 1, MOD is 1000000007, a is a list of length n filled with lists of integers obtained by mapping int to the input split by spaces, _ is n
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: N is a positive integer, values of a_{i,j} are either 0 or 1, MOD is 1000000007, a is a list of length n filled with lists of integers obtained by mapping int to the input split by spaces, _ is n, dp is a 2D list of dimensions (n+1) x (2^n) where the first row is filled with 1s
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: After the loop has executed completely, `i` is equal to `n + 1`, `dp` has been fully updated with the modulo operation using `MOD`, `N` is a positive integer, values of `a_{i,j}` are either 0 or 1, `MOD` is 1000000007, `a` is a list of length n filled with lists of integers, `_` is n, and `mask` is less than `1 << n`. The values of `dp[i][mask]` have been updated based on the provided formula for all valid combinations of `i` and `mask`.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function `func` reads input values to construct a matrix of size N x N, where each element a_{i,j} can be either 0 or 1. It then performs calculations on this matrix using dynamic programming techniques to calculate and print a specific value. The function does not accept any parameters and works solely based on the input data provided during execution.

