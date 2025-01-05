#State of the program right berfore the function call: N is an integer such that 1 <= N <= 21, and a_{i, j} is either 0 or 1 for all i, j where 1 <= i, j <= N.**
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: MOD is 1000000007, `n` is greater than 0, `a` is appended with the result of mapping integers from input split for n times
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: MOD is 1000000007, `n` is greater than 0, `a` is appended with the result of mapping integers from input split for n times, dp is a 2D list with n + 1 rows and 2^n columns filled with ones
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, MOD is 1000000007, n is greater than 0, a is appended with the result of mapping integers from input split for n times, dp is a 2D list with n + 1 rows and 2^n columns filled with the updated values based on the conditions provided in the loop code.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function `func` reads an integer `n` as input, followed by a 2D array `a` of size n x n with binary values. It then performs a dynamic programming algorithm to calculate and update values in a 2D list `dp`. Finally, it prints the value at position `(1 << n) - 1` in the last row of `dp`. The function does not accept any parameters and operates solely on the input provided during execution.

