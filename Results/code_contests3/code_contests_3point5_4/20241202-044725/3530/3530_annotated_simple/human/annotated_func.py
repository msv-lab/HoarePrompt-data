#State of the program right berfore the function call: **
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: `MOD` is 1000000007, `n` is a positive integer, `a` contains the input values as integers for each iteration, `_` is equal to `n`.
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `MOD` is 1000000007, `n` is a positive integer, `a` contains the input values as integers for each iteration, `_` is equal to `n`, a 2D list `dp` is created with dimensions `(n + 1) x (1 << n)` filled with zeros, `dp[0][i]` is assigned the value 1 for all i from 0 to (1 << n) - 1
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, the values of MOD, n, a, _, and dp remain the same as the initial state. The loop updates the values in the 2D list dp according to the conditions specified in the loop code. The final state will depend on the input values in list 'a' and how they satisfy the conditions a[i - 1][j] == 1 and mask & 1 << j for all iterations of the loop.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function `func` initializes a list `a` with integers based on user input, creates a 2D list `dp`, and performs calculations to update values in `dp` according to certain conditions. Finally, it prints a specific value from `dp` based on the input. The function does not accept any parameters.

