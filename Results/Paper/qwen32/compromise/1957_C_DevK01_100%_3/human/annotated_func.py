#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and k is an integer such that 0 <= k <= n. Each of the next k lines contains two integers r_i and c_i, denoting the i-th move you made, where 1 <= r_i, c_i <= n. It is guaranteed that the sum of n over all test cases does not exceed 3 * 10^5.
def func_1(n):
    dp = [1, 1]
    for i in range(2, n + 1):
        dp += [(dp[-1] + 2 * (i - 1) * dp[-2]) % (7 + 10 ** 9)]
        
        dp.pop(0)
        
    #State: [dp[n-1], dp[n]]
    return dp[-1]
    #The program returns dp[n]
#Overall this is what the function does:The function accepts an integer `n` such that 1 <= n <= 3 * 10^5 and returns the value of `dp[n]`, which is computed based on a specific recursive formula modulo 10^9 + 7.

