#State of the program right berfore the function call: N is an integer such that 1 <= N <= 21, and a is a 2D list of integers where each element is either 0 or 1, with dimensions N x N.
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 <= N <= 21; `a` is a 2D list containing `n` rows of integers from input; `MOD` is 1000000007; `n` is a string representing an integer greater than or equal to 0; `_` is `n-1` if `n` is greater than 0, or `-1` if `n` is 0.
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `dp` is a 2D list of size `(n + 1) x (1 << n)`, where `dp[0][i]` is 1 for all `i` less than `1 << n`, and other entries remain zeros.
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: `dp` is a 2D list of size `(n + 1) x (1 << n)`, where `dp[i][mask]` contains the cumulative number of ways to achieve the configuration represented by `mask` using the first `i` elements of `a`, based on the conditions defined in the loop. Specifically, if `a[i - 1][j]` is 1 and the j-th bit of `mask` is set, then `dp[i][mask]` is updated by the sum of `dp[i - 1][mask ^ 1 << j]` across all valid `j`. If no conditions are met during the iterations, `dp[i][mask]` remains unchanged from the previous values.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function accepts an integer `N` (where 1 <= N <= 21) and a 2D list `a` of size `N x N` containing integers (0 or 1). It calculates and prints the number of valid configurations represented by a bitmask using dynamic programming. Specifically, it counts the ways to select elements based on the conditions defined in the list `a`, where a `1` indicates that the corresponding element can be selected. The function ultimately returns the count of configurations that use all `N` elements. It does not handle invalid inputs or cases where `N` is outside the specified range.

