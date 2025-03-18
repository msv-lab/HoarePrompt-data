#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 3⋅10^5, k is an integer such that 0 ≤ k ≤ n, and for each test case, r_i and c_i are integers such that 1 ≤ r_i, c_i ≤ n and the k moves and the implied computer moves are valid.
def func_1(n):
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007
        
    #State: Output State: The final state of `dp` will be a list where each element `dp[i]` (for 1 ≤ i ≤ n) is computed as `(dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007` for all `i` from 3 to `n`. After executing all iterations of the loop, the value of `i` will be `n + 1`, and `n` must be greater than or equal to the maximum index in the `dp` array, which is `n`.
    #
    #In simpler terms, after the loop completes all its iterations, the `dp` array will contain values calculated according to the given formula for each index from 3 to `n`, with all other variables remaining in their initial or updated states as described.
#Overall this is what the function does:The function accepts an integer \( n \) where \( 1 \leq n \leq 3 \times 10^5 \) and computes a dynamic programming array `dp` of length \( n+1 \). Each element `dp[i]` (for \( 1 \leq i \leq n \)) is calculated using the formula `(dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007`. After completing the computation, the function returns nothing, leaving the `dp` array populated with the computed values.

