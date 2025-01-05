#State of the program right berfore the function call: **Precondition**: **N is a positive integer, 1 <= N <= 21. The compatibility matrix a_{i, j} is a 2D list of integers where 0 <= a_{i, j} <= 1.**
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: Output State: MOD is assigned the value 1000000007, `n` holds the input value, `a` is a list containing the mapped integer values from the input split for each iteration of the loop.
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: MOD is assigned the value 1000000007, `n` is a non-negative integer, `a` contains mapped integer values, `dp` is a 2D list of dimensions (n+1) x (1 << n) initialized with 0s, all elements in dp[0] are assigned the value 1
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: MOD is 1000000007, `n` is a non-negative integer greater than or equal to 1, `a` contains mapped integer values, `dp` is a 2D list of dimensions (n+1) x (1 << n) where dp[0] is all 1s. The values in the dp array have been updated for all iterations of `i`, `mask`, and `j` based on the conditions in the loop code.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function `func` reads an integer input `n`, then reads a 2D matrix `a` of size n x n. It initializes a dynamic programming array `dp` and fills it based on certain conditions. Finally, it prints a specific value from the `dp` array. The function does not accept any parameters and does not return any value.

