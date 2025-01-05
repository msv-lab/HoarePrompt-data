#State of the program right berfore the function call: N is an integer such that 1 <= N <= 21, and a is a 2D list of integers (0 or 1) representing the compatibility of N men and N women, where a[i][j] indicates if Man i and Woman j are compatible.
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 <= `N` <= 21; `a` is a 2D list with `n` rows of integers from input; `MOD` is 1000000007; `_` is `n - 1` (where `n` is the number of iterations executed).
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 <= `N` <= 21, `n` is at least 1, `i` is (2^n - 1), and `dp[0][i]` is 1 for all `i` from 0 to (2^n - 1).
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 <= `N` <= 21, `n` is at least 1, `i` is `n`, `mask` is in the range from 1 to \(2^n - 1\), and `dp[n][mask]` reflects the cumulative updates based on the conditions evaluated for all `j` from 0 to `n - 1`, considering all valid states for the given `mask`.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function accepts an integer `n` (where 1 <= n <= 21) and a 2D list `a` of integers (0 or 1) that indicates compatibility between `n` men and `n` women. It computes the number of ways to pair all men with women based on their compatibility using dynamic programming and returns this count modulo 1000000007. The output is the number of valid pairings for all `n` men and `n` women.

