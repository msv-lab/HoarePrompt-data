#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and k is an integer such that 0 ≤ k ≤ n. Each of the next k lines contains two integers r_i and c_i, denoting the i-th move you made, where 1 ≤ r_i, c_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1(n):
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 3 ≤ n ≤ 3 · 10^5, `k` is an integer such that 0 ≤ k ≤ n, each of the next k lines contains two integers r_i and c_i, denoting the i-th move you made, where 1 ≤ r_i, c_i ≤ n, `dp[1]` is 1, `dp[2]` is 3, `dp[3]` is 7, `dp[4]` is 25, `dp[5]` is 81, ..., `dp[n]` is the value computed by the loop, `i` is n+1.
#Overall this is what the function does:The function `func_1` computes and returns the value of `dp[n]` based on a specific recursive formula, where `dp[i]` is calculated using the values of `dp[i-1]` and `dp[i-2]`. The function takes an integer `n` as input, with the constraint `1 ≤ n ≤ 3 · 10^5`, and returns the computed value modulo 1000000007.

