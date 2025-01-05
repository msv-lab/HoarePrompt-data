#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 21, and a is a 2D list of integers where each element is either 0 or 1, representing the compatibility between N men and N women.
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 21, `a` is a 2D list containing `N` rows, each populated with integers from the input, `MOD` is 1000000007, `n` is a string that converts to an integer equal to `N`.
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 21, `n` is equal to `N`, `dp[0][i]` is 1 for all `i` from 0 to \(2^N - 1\).
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 21; `n` is equal to `N`; `dp[n][mask]` contains the computed values based on all valid combinations of `mask` and `j`, representing the accumulation of previous states modulo `MOD` for all masks from 1 to `2^N - 1`.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function reads an integer `N` and a 2D list `a` of size `N x N`, where each element indicates compatibility (0 or 1) between `N` men and `N` women. It computes the number of valid ways to pair all men with women such that each man is paired with a compatible woman, using dynamic programming and returns this count modulo `1000000007`. The function does not handle any input errors or constraints explicitly beyond the initial assumption that `N` is between 1 and 21.

