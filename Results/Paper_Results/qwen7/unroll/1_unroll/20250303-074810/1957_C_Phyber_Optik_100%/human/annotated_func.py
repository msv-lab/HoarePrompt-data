#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3⋅10^5 and 0 ≤ k ≤ n. The pairs (r_i, c_i) for i-th move you made are such that 1 ≤ r_i, c_i ≤ n and the moves are valid (no two rooks attack each other). The sum of n over all test cases does not exceed 3⋅10^5.
def func_1(n):
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007
        
    #State: Output State: dp is a list where dp[i] for 1 ≤ i ≤ n contains the value computed by the loop for each respective i, with all values calculated modulo 1000000007.
#Overall this is what the function does:The function accepts an integer `n` such that 1 ≤ n ≤ 3⋅10^5. It computes a list `dp` where `dp[i]` for 1 ≤ i ≤ n contains the value `(dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007` for each respective `i`. After the function concludes, `dp` is returned, representing the computed values under the specified conditions.

