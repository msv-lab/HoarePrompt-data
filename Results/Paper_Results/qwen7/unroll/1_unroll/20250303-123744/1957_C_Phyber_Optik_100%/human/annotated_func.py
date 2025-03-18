#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 0 ≤ k ≤ n. Additionally, r_i and c_i are integers such that 1 ≤ r_i, c_i ≤ n for each move i, and the k moves and the implied computer moves are valid. The sum of n over all test cases does not exceed 3 ⋅ 10^5.
def func_1(n):
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007
        
    #State: Output State: `dp[i]` for each `i` from 3 to `n` is calculated using the formula `(dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007`, starting with `dp[1]` as 1 and `dp[2]` as 3.
#Overall this is what the function does:The function accepts an integer \( n \) and calculates the values of the array \( dp \) from index 1 to \( n \) using the specified formula. Specifically, \( dp[1] \) is set to 1, \( dp[2] \) is set to 3, and for each \( i \) from 3 to \( n \), \( dp[i] \) is computed as \( (dp[i - 1] + 2 \times (i - 1) \times dp[i - 2]) \mod 1000000007 \). The final state of the program includes the computed values of \( dp[i] \) for all \( i \) from 1 to \( n \).

