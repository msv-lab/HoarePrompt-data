#State of the program right berfore the function call: m is an integer such that 1 <= m <= 10^9, a and b are positive integers such that 1 <= a, b <= 10^5.
def func():
    m, a, b = map(int, input().split())

dp = [0] * (m + 1)

dp[0] = 1
    for i in range(m + 1):
        if i + a <= m:
            dp[i + a] += dp[i]
        
        if i - b >= 0:
            dp[i] += dp[i - b]
        
    #State of the program after the  for loop has been executed: `i` is `m`, `m` is an integer such that 1 ≤ m ≤ 10^9, `a` is a positive integer such that 1 ≤ a ≤ 10^5, `b` is a positive integer such that 1 ≤ b ≤ 10^5, `dp` is a list of length `m+1` where all elements are 0 except `dp[0]` which is 1.
    print(sum(dp))
#Overall this is what the function does:The function reads three integers \(m\), \(a\), and \(b\) from input, where \(1 \leq m \leq 10^9\) and \(1 \leq a, b \leq 10^5\). It then constructs a dynamic programming array `dp` of length \(m+1\) initialized to zero, with `dp[0]` set to 1. For each index `i` from 0 to \(m\), it updates `dp[i+a]` and `dp[i-b]` if the indices are within bounds. After completing the loop, it prints the sum of all elements in the `dp` array. The function effectively computes a modified version of a knapsack problem where it counts the number of ways to reach each index in the array by adding `a` or subtracting `b` from previous indices. The final state of the program is that the sum of the `dp` array is printed, representing the total count of valid paths. Edge cases include the possibility of negative indices when subtracting `b`, which are handled by setting `dp[i]` to `dp[i-b]` only if `i - b` is non-negative.

