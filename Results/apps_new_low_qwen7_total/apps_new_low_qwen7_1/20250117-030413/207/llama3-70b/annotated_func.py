#State of the program right berfore the function call: m is a non-negative integer such that \(1 \leq m \leq 10^9\), and a and b are positive integers such that \(1 \leq a, b \leq 10^5\).
def func():
    m, a, b = map(int, input().split())

dp = [0] * (m + 1)

dp[0] = 1
    for i in range(m + 1):
        if i + a <= m:
            dp[i + a] += dp[i]
        
        if i - b >= 0:
            dp[i] += dp[i - b]
        
    #State of the program after the  for loop has been executed: m is m_val, a is a_val, b is b_val, and dp is a list of length m_val + 1 where each element dp[i] represents the number of ways to sum up to i using multiples of a and/or b starting from 0. Specifically, dp[0] is 1 (base case), and for any i from 1 to m_val, dp[i] is the sum of dp[i - b] and dp[i - a] if both indices are valid, otherwise dp[i] remains 0.
    print(sum(dp))
#Overall this is what the function does:The function `func()` accepts three non-negative integer inputs `m`, `a`, and `b` such that \(1 \leq m \leq 10^9\) and \(1 \leq a, b \leq 10^5\). It calculates the number of ways to sum up to `m` using multiples of `a` and/or `b` starting from 0. The function initializes a list `dp` of length `m + 1` where `dp[i]` represents the number of ways to sum up to `i` using `a` and `b`. The base case is set to `dp[0] = 1`. For each index `i` from 0 to `m`, the function updates `dp[i]` by adding the values of `dp[i - b]` and `dp[i - a]` if the indices are within bounds. After the loop, the function prints the sum of all elements in `dp`, which represents the total number of ways to sum up to `m` using `a` and `b`.

Potential edge cases:
- If `m` is 0, the function will return 1 because `dp[0]` is initialized to 1.
- If `a` or `b` is 1, the function will handle these cases correctly since the loop updates `dp[i]` appropriately for such values.

Missing functionality:
- The function does not handle negative values for `m`, `a`, or `b`. However, given the constraints, the inputs are guaranteed to be non-negative and within the specified ranges.

