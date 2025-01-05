#State of the program right berfore the function call: **
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: MOD is 1000000007, `a` is a list containing n lists of integers obtained from the input split
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `MOD` is 1000000007, `a` is a list containing n lists of integers obtained from the input split, `dp` is a 2D list with dimensions (n+1) x (1 << n) where all elements are 1, `i` is (1 << n)
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have executed, the final values in `dp[i][mask]` will be updated according to the conditions specified in the loop code, taking into account the values in the `a` list and the operations performed on `dp[i][mask]`. The values of MOD, `a`, `dp`, `i`, `j`, and `mask` will remain consistent with their initial definitions.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function `func` initializes a variable `MOD` with the value 1000000007, reads an integer `n` from input, and then populates a list `a` with `n` lists of integers obtained from the split input. It then creates a 2D list `dp` with dimensions (n+1) x (1 << n) and fills it with ones. Subsequently, it iterates through nested loops to update the values in `dp` based on conditions involving the elements in list `a`. Finally, it prints a specific value from `dp` based on the calculations performed earlier. The function does not accept any parameters and does not have explicit return values.

