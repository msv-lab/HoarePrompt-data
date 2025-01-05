#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 21, and a is a 2D list of integers where each element a[i][j] is either 0 or 1, representing the compatibility between Man i and Woman j.
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 21; `a` contains a list of `N` maps, each map object representing the integers from user input; `MOD` is 1000000007.
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 21; `dp[0]` is a list where all elements are 1, and `i` is `1 << n` (which is 2^n).
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 21; `mask` ranges from 1 to `2^N - 1`; `dp[N][mask]` contains the cumulative results of valid transitions based on the conditions checked for all `j` in the range `N`. After all iterations of the loop, `dp[i][mask]` reflects the cumulative updates based on all values of `i` from 1 to `N`, with `dp[i][mask]` representing the total number of valid configurations considering all conditions defined by the adjacency matrix `a`.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function accepts a positive integer `N` (where 1 <= N <= 21) and a 2D list `a` of integers (0 or 1) that represent the compatibility between `N` men and `N` women. It calculates the number of valid pairings based on this compatibility matrix using dynamic programming and outputs the total number of valid configurations where each man is paired with exactly one woman, considering all compatibility constraints. The result is computed modulo 1000000007.

