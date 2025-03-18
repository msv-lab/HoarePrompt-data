#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3 · 10^5 and 0 ≤ k ≤ n. The sum of n over all test cases does not exceed 3 · 10^5. Each of the next k lines contains two integers r_i and c_i, denoting the i-th move you made, where 1 ≤ r_i, c_i ≤ n. It is guaranteed that the k moves and the implied computer moves are valid.
def func_1(n):
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007
        
    #State: The values of `dp[i]` for `i` from `3` to `n` are computed using the formula `dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007`, with `dp[1]` remaining `1` and `dp[2]` remaining `3`. All other variables (`t`, `n`, `k`, and the moves `r_i` and `c_i`) remain unchanged.
#Overall this is what the function does:The function `func_1` computes and stores a sequence of values in a list `dp` up to the index `n` using a specific recursive formula. The values are computed modulo 1000000007. The function does not return any value.

