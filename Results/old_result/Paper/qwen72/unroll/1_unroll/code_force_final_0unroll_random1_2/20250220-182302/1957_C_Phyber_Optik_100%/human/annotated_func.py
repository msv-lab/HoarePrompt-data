#State of the program right berfore the function call: n is an integer representing the size of the chessboard, such that 1 ≤ n ≤ 3 · 10^5.
def func_1(n):
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007
        
    #State: `dp[n]` is the value computed by the loop, which is `(dp[n - 1] + 2 * (n - 1) * dp[n - 2]) % 1000000007`.
#Overall this is what the function does:The function `func_1` accepts an integer `n` (where 1 ≤ n ≤ 3 · 10^5) and computes a value `dp[n]` based on a dynamic programming approach. The final state of the program is that `dp[n]` holds the computed value, which is the result of a specific recurrence relation modulo 1000000007. The function does not return any value, but the computed `dp[n]` can be used for further processing or output.

