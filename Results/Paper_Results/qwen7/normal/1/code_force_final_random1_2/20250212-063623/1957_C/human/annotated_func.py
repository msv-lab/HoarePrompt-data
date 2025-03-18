#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 0 ≤ k ≤ n; for each test case, r_i and c_i are integers such that 1 ≤ r_i, c_i ≤ n and the moves are valid according to the problem description.
def func_1(n):
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007
        
    #State: dp[1] is 1, dp[2] is 3, dp[3] is 5, dp[4] is 11, dp[5] is 23, dp[6] is 35, and so on until dp[n] has been calculated, t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 0 ≤ k ≤ n, i is n + 1.
#Overall this is what the function does:The function accepts an integer `n` and calculates a sequence of integers stored in the list `dp`, where `dp[i]` represents the number of ways to tile a 2 × i rectangle with 1 × 2 dominoes and 2 × 2 squares, modulo 1000000007. After calculating up to `dp[n]`, the function does not return any specific value.

