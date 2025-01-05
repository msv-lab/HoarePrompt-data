#State of the program right berfore the function call: N is an integer such that 1 <= N <= 21, and a is a 2D list of integers where a[i][j] is either 0 or 1, representing the compatibility of Man i and Woman j for all 1 <= i, j <= N.
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 <= `N` <= 21, `a` is a list containing `n` map objects of integers from input, `MOD` is 1000000007, `_` is `n-1.
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 <= `N` <= 21, `a` is a list containing `n` map objects of integers from input, `MOD` is 1000000007, `_` is `n - 1`, `dp[0][i]` is 1 for all valid `i` less than `2^n`, and all other values in `dp` remain zero.
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: `dp[n][mask]` contains the final values after processing all combinations of `mask` for `j` from 0 to `n-1`, where `mask` ranges from `1` to `2^n - 1`, `N` is an integer such that 1 <= `N` <= 21, `n` is the final value of `n` after all iterations.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function accepts an integer `n` (1 <= n <= 21) and a 2D list `a` (where a[i][j] is either 0 or 1), calculates the number of perfect matchings based on compatibility, and prints the result.

