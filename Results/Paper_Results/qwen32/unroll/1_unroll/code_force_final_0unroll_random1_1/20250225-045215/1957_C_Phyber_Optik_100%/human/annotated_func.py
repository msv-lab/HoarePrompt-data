#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and k is an integer such that 0 ≤ k ≤ n. Each of the next k lines contains two integers r_i and c_i, where 1 ≤ r_i, c_i ≤ n, representing the i-th move you made. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1(n):
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007
        
    #State: The `dp` array is fully computed from `dp[1]` to `dp[n]` using the provided recurrence relation. The specific values of `dp[3]` to `dp[n]` depend on the value of `n` and are calculated as follows:
    #- `dp[1]` remains 1.
    #- `dp[2]` remains 3.
    #- For `i` from 3 to `n`, `dp[i]` is calculated using the formula `dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007`.
    #The values of `r_i` and `c_i` provided in the input do not affect the computation of the `dp` array in this loop.
#Overall this is what the function does:The function `func_1` computes and returns the value of `dp[n]` using a specific recurrence relation, where `dp` is an array initialized with `dp[1] = 1` and `dp[2] = 3`. The computation involves iterating from 3 to `n` and updating `dp[i]` based on the formula `dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007`. The function accepts a single integer parameter `n` and does not utilize any other input parameters such as `k`, `r_i`, or `c_i`.

