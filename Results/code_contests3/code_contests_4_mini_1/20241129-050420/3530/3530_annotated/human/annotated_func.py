#State of the program right berfore the function call: N is an integer such that 1 <= N <= 21, and a is a 2D list of integers where each element is either 0 or 1, representing the compatibility between N men and N women, with dimensions N x N.
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 <= `N` <= 21; `a` contains a list with `n` entries from the input integers; `MOD` is 1000000007.
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `dp` is a list of size `n + 1` where each entry is a list of size `2^n`, and `dp[0][i]` is set to 1 for all `i` in the range `0` to `2^n - 1`.
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: `dp` is a list of size `n + 1` where each entry is a list of size `2^n`, and `dp[n][mask]` contains the cumulative contributions from valid states based on the conditions involving `a[i - 1][j]` and `mask & 1 << j`, with each entry taken modulo `MOD`, for all `mask` in the range from `1` to `2^n - 1`.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function accepts an integer `N` (where 1 <= N <= 21) and a 2D list `a` of dimensions N x N, where each element is either 0 or 1, indicating compatibility between N men and N women. It calculates the total number of valid pairings of men and women based on this compatibility matrix and outputs the result modulo 1000000007. The function does not handle cases where the input `N` or the compatibility matrix might be invalid; it assumes valid input.

