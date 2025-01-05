#State of the program right berfore the function call: N is a positive integer, and a_{i,j} values are either 0 or 1.**
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: N is a positive integer, a_{i,j} values are either 0 or 1, MOD is 1000000007, `n` is assigned the input value, `a` is a list containing lists of integers converted from input values for each iteration of the loop
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: N is a positive integer, `n` is a valid positive integer, `a` is a list containing lists of integers converted from input values for each iteration of the loop, dp is a 2D list initialized with 0 values of size (1 << n) for each row in range n+1, `i` is (1 << n), dp[0][(1 << n)] is assigned the value 1. After executing the code snippet, all dp[0][i] for i ranging from 0 to (1 << n) are assigned the value 1.
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, the values of `dp[i][mask]`, `i`, `mask`, `n`, and `a` will be updated according to the loop logic. The loop will execute for `n` times, and `dp[i][mask]` will be updated based on the conditions specified in the loop by adding `dp[i - 1][mask ^ 1 << j]` if `a[i - 1][j] == 1` and `mask & 1 << j`. The updated values will be taken modulo `MOD`.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function `func` reads a positive integer `N` and a matrix of 0s and 1s represented as `a_{i,j}`. It then calculates and updates a 2D list `dp` based on specific conditions. Finally, it prints the value stored in `dp[n][(1 << n) - 1]`, without explicitly returning a value.

