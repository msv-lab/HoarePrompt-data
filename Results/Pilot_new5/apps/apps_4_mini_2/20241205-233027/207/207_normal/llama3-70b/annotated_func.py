#State of the program right berfore the function call: m is a positive integer such that 1 <= m <= 10^9, a and b are positive integers such that 1 <= a, b <= 10^5.
def func():
    m, a, b = map(int, input().split())
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(m + 1):
        if i + a <= m:
            dp[i + a] += dp[i]
        
        if i - b >= 0:
            dp[i] += dp[i - b]
        
    #State of the program after the  for loop has been executed: `dp` is a list of length `m + 1`, where `dp[0]` is 1, and for each index `i` (1 <= `i` <= `m`), `dp[i]` is the sum of `dp[i - b]` for all valid indices `i - b` and the number of ways to reach index `i + a` from index `i`, which adds `dp[i]` to `dp[i + a]` if `i + a <= m`. If the loop does not execute, then `dp` remains unchanged with `dp[0]` as 1 and all other elements as 0.
    print(sum(dp))
#Overall this is what the function does:The function accepts three positive integers, `m`, `a`, and `b`, from user input and computes the number of distinct ways to reach a total of `m` by either adding `a` or subtracting `b` in each step. It returns the sum of all ways to reach each index from 0 to `m`, where the initial state has one way (starting at 0). If `m` is less than `a` or less than `b`, it appropriately handles those cases by ensuring that indices remain within valid bounds. The function does not explicitly return a value; instead, it prints the computed sum.

