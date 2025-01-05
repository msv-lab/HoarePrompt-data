#State of the program right berfore the function call: **
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: MOD is 1000000007, n is greater than 0, a contains a list of n lists of integers from the input, _ is n-1
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: MOD is 1000000007, n is greater than 0, a contains a list of n lists of integers from the input, _ is n-1, dp is a 2D list of size (n+1) x (2^n) with all elements of dp[0] initialized to 1
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: At the end of the loop execution, `MOD`, `n`, `a`, `_`, `dp`, `i`, `mask`, `j` are all within the specified range. The final value of `dp[i][mask]` is the result of updating it by taking its modulo with `MOD` for every execution of the loop where `a[i - 1][j]` is equal to 1 and the j-th bit of `mask` is set for all possible combinations of `mask` and `j`.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function initializes a 2D list `dp`, performs calculations on this list based on the input values `n` and `a`, and finally prints a specific value from the `dp` list. The function does not accept any parameters and operates solely based on the internal logic.

