#State of the program right berfore the function call: **
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: MOD is 1000000007, `a` is a list containing the integer values obtained from all the input splits
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `MOD` is 1000000007, `a` is a list containing the integer values obtained from all the input splits, `dp` is a 2D list with all elements set to 1, `i` is equal to `1 << n - 1`, `n` is a non-negative integer to determine the number of iterations
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: After all the iterations of the loop have finished, MOD remains 1000000007, `a` still contains integer values, `dp` holds the final updated values based on the loop conditions, `i` is 1 << n, `n` is a non-negative integer greater than or equal to 1, `mask` is equal to (1 << n) - 1, and `j` is equal to n - 1. The loop has iterated over all possible combinations of `mask` and `j`, updating `dp[i][mask]` based on the conditions specified in the loop code.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function `func` initializes MOD as 1000000007, reads an integer `n` from input, and populates a list `a` with integer values obtained from subsequent input splits. It then creates a 2D list `dp` and performs nested loops to update its values based on certain conditions. Finally, the function prints a specific output based on the updated `dp` values. The function does not accept any parameters explicitly.

