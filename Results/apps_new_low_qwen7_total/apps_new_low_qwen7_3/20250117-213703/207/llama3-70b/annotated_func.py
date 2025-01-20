#State of the program right berfore the function call: m, a, and b are integers such that \(1 \leq m \leq 10^9\) and \(1 \leq a, b \leq 10^5\).
def func():
    m, a, b = map(int, input().split())

dp = [0] * (m + 1)

dp[0] = 1
    for i in range(m + 1):
        if i + a <= m:
            dp[i + a] += dp[i]
        
        if i - b >= 0:
            dp[i] += dp[i - b]
        
    #State of the program after the  for loop has been executed: `dp` is a list of length `m+1` where `dp[0] = 1` and for each `i` from `1` to `m`, `dp[i]` is the sum of all previous `dp[j]` values such that `j + a <= i` and `j - b >= 0`.
    print(sum(dp))
#Overall this is what the function does:The function reads three integers \(m\), \(a\), and \(b\) from input, where \(1 \leq m \leq 10^9\) and \(1 \leq a, b \leq 10^5\). It then initializes a list `dp` of length \(m+1\) with all elements set to 0, except for `dp[0]` which is set to 1. The function iterates over the range from 0 to \(m\) and updates the `dp` list based on the values of \(a\) and \(b\): for each index \(i\), it adds the value of `dp[i-a]` to `dp[i+a]` and the value of `dp[i+b]` to `dp[i]`. After the iteration, it prints the sum of all elements in the `dp` list. This sum represents the number of ways to reach the index \(m\) using steps of size \(a\) or \(-b\).

