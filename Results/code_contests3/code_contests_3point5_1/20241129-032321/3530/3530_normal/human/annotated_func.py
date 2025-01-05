#State of the program right berfore the function call: N is a positive integer, and a_{i, j} is either 0 or 1 for all i, j where 1 <= i, j <= N.**
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: `N` is a positive integer, `a_{i, j}` is either 0 or 1 for all i, j where 1 <= i, j <= N, MOD is 1000000007, `n` is the user input and greater than 0, `a` contains the integers obtained from the user input split by space, `_` is equal to n-1 for the loop to execute
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer, `a_{i, j}` is either 0 or 1 for all i, j where 1 <= i, j <= N, MOD is 1000000007, `n` is the user input and greater than 0, `a` contains the integers obtained from the user input split by space, `_` is equal to n-1, `dp` is a 2D list with dimensions (n+1) x (1 << n) where the value at index 0 of each subarray is initialized to 1 for all i in range(1 << n)
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, the values of all variables `N`, `a_{i, j}`, `MOD`, `n`, `a`, `_`, `dp`, `mask`, and `j` will remain the same as their initial values before the loop started. The only variable that will be updated is `dp[i][mask]` for all valid values of i, mask, and j following the provided formula and taking the modulo with the value of MOD.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function `func` reads a positive integer `n` from the user as input, then reads an `n x n` matrix `a` consisting of elements that are either 0 or 1. It calculates and updates a dynamic programming array `dp` based on the provided formula and constraints. Finally, it prints the value at a specific index of `dp` without returning a value.

