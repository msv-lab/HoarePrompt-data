#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 21, and a is a 2D list of integers where each element is either 0 or 1, with dimensions N x N.
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 21; `a` is a 2D list containing `n` rows of integers from user input; `MOD` is 1000000007; `_` is `n-1` if `n` > 0, otherwise `_` is -1 (indicating no iterations).
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 21; `a` is a 2D list containing `n` rows of integers from user input; `MOD` is 1000000007; `_` is `n-1` if `n` > 0, otherwise `_` is -1; `dp[0][i]` is 1 for all `i` in the range 0 to `2^n - 1`.
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 21, `n` is a positive integer, `i` is `n`, `mask` has been evaluated for all values from 1 to \( 2^n - 1 \), `dp[i][mask]` contains the accumulated values based on the conditions checked across all indices `j` from 0 to `n-1` in the array `a`, and the values are taken modulo `MOD`.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function accepts an integer `N` (where 1 <= N <= 21) and a 2D list `a` of integers (with dimensions N x N) where each element is either 0 or 1. It calculates a dynamic programming table to determine the number of ways to select elements from the list based on the conditions in `a`, and finally prints the count of valid selections modulo `1000000007`. The function does not handle cases where the input might be invalid or where `N` does not meet the specified constraints.

