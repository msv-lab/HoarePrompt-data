#State of the program right berfore the function call: n is an integer representing the size of the chessboard, where 1 ≤ n ≤ 3 × 10^5.
def func_1(n):
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007
        
    #State: After the loop has executed all iterations, `n` remains the same as the initial value, `i` is `n + 1`, `dp[1]` is 1, `dp[2]` is 3, and `dp[n]` contains the final computed value based on the given recurrence relation.
#Overall this is what the function does:The function `func_1` accepts an integer `n` (where 1 ≤ n ≤ 3 × 10^5) representing the size of a chessboard. It computes a sequence `dp` using a specific recurrence relation and stores the result up to `dp[n]`. The function does not return any value explicitly, but after its execution, the array `dp` will have `dp[1] = 1`, `dp[2] = 3`, and `dp[n]` will contain the final computed value based on the recurrence relation `(dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007`. The input parameter `n` remains unchanged.

