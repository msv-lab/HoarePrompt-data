#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 3⋅10^5, k is an integer such that 0 ≤ k ≤ n, and for each test case, r_i and c_i are integers such that 1 ≤ r_i, c_i ≤ n and the k moves and the implied computer moves are valid.
def func_1(n):
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 3⋅10^5, `k` is an integer such that 0 ≤ k ≤ n, `dp[1]` is 1, `dp[2]` is 3, and for all `i` in the range 3 to `n`, `dp[i]` is calculated as `(dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007`.
#Overall this is what the function does:The function accepts an integer `n` and computes a dynamic programming array `dp` where `dp[i]` represents the number of ways to reach the `i-th` position under certain constraints. Specifically, for each `i` from 3 to `n`, `dp[i]` is calculated as `(dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007`. After executing the function, the array `dp` contains precomputed values up to `n`, with `dp[1]` set to 1 and `dp[2]` set to 3.

