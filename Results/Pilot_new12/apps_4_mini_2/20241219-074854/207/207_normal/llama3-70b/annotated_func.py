#State of the program right berfore the function call: m is a positive integer such that 1 <= m <= 10^9, a is a positive integer such that 1 <= a <= 10^5, and b is a positive integer such that 1 <= b <= 10^5.
def func():
    m, a, b = map(int, input().split())
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(m + 1):
        if i + a <= m:
            dp[i + a] += dp[i]
        
        if i - b >= 0:
            dp[i] += dp[i - b]
        
    #State of the program after the  for loop has been executed: `dp` is a list of length `m + 1`, `dp[0]` is 1, `dp[1] to dp[m]` represent the count of ways to reach each index based on the provided input integers `a` and `b` with respect to the initial integer `m`.
    print(sum(dp))
#Overall this is what the function does:The function accepts three positive integers, m, a, and b. It calculates the number of ways to reach each index from 0 to m using steps of size a (moving forward) and b (moving backward) and stores the result in a list dp. After processing the entire range from 0 to m, it sums up all the values in the dp list and prints the total. This sum represents the total number of distinct ways to arrive at each index from the starting point (0) under the given constraints. It's important to note that due to the constraints provided, particularly the large possible value of m (up to 10^9), the implementation may face performance issues with memory and time complexity, as constructing a dp list of this size could be impractical. The function does not return any value explicitly but prints the computed result.

