#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3⋅10^5 and 0 ≤ k ≤ n. The coordinates (r_i, c_i) for each move you made are integers such that 1 ≤ r_i, c_i ≤ n, and no two rooks share the same row or column after each move and its mirrored move by the computer.
def func_1(n):
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007
        
    #State: Output State: `dp` is a list where `dp[1]` is 1, `dp[2]` is 3, `dp[3]` is 5, `dp[4]` is 11, `dp[5]` is 29, `dp[6]` is 17, `dp[7]` is 89, `dp[8]` is 239, `dp[9]` is 719, `dp[10]` is 2081, and so on until `dp[n]` is calculated for the maximum `n` which is \(3 \times 10^5\), `t` is an integer such that \(1 \leq t \leq 10^4\), `n` is an integer such that \(1 \leq n \leq 3 \times 10^5\), `k` is an integer such that \(0 \leq k \leq n\), and `i` is greater than `n`.
    #
    #This output state represents the final state of the `dp` array after the loop has executed for all iterations up to `n`, with the given recurrence relation applied. The values in `dp` follow the pattern defined by the loop, starting from the initial conditions provided and extending up to the maximum possible value of `n`.
#Overall this is what the function does:The function calculates a dynamic programming array `dp` of size `n+1` where `dp[i]` represents a specific value determined by the recurrence relation `dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007`. The function initializes `dp[1]` to 1 and `dp[2]` to 3, then iteratively computes the values for `dp[i]` from 3 to `n`. After completing these calculations, the function returns the entire `dp` array, which contains the computed values up to `dp[n]`.

