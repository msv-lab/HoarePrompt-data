#State of the program right berfore the function call: n is a positive integer representing the size of the chessboard, and the function is designed to handle a single test case without the additional parameters for multiple test cases or the moves made.
def func_1(n):
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007
        
    #State: `dp[n]` is the value calculated by the loop as `(dp[n - 1] + 2 * (n - 1) * dp[n - 2]) % 1000000007`.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` representing the size of a chessboard. It initializes a dynamic programming array `dp` with `dp[1] = 1` and `dp[2] = 3`. The function then calculates `dp[n]` using a loop that iterates from 3 to `n`, updating `dp[i]` based on the formula `(dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007`. After the loop, the function returns `dp[n]`, which represents the result of the computation for a chessboard of size `n`.

