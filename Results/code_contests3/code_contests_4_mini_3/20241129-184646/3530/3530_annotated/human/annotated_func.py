#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 21, and a is a 2D list of integers with dimensions N x N, where each element a[i][j] is either 0 or 1, indicating the compatibility between Man i+1 and Woman j+1.
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 21; `a` is a 2D list with `n` rows of integers added from input; `MOD` is 1000000007; `n` is a string convertible to an integer greater than 0.
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 21, `n` is a string convertible to an integer greater than 0, `i` is `2^n`, `dp[0][i]` is 1 for all `i` in the range from 0 to `2^n - 1`.
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that `1 <= N <= 21`, `n` is a string convertible to an integer greater than or equal to 1, `mask` is in the range from `0` to `2^n - 1`, `j` is in the range from `0` to `n - 1`, and `dp[i][mask]` contains the accumulated values based on all valid combinations of `i`, `mask`, and `j` as per the conditions in the nested loops, reflecting the contributions from previous iterations and valid states of `dp`.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function accepts a positive integer `N` and a 2D list `a` of dimensions N x N, where each element indicates the compatibility between men and women. It calculates the number of valid pairings based on the compatibility data and prints the result modulo 1000000007. The function assumes valid input but does not handle cases where `N` is outside the specified range or invalid input types.

