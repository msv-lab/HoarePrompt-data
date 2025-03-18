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
        
    #State of the program after the  for loop has been executed: Output State:
    print(sum(dp))
#Overall this is what the function does:The function reads three integers \( m \), \( a \), and \( b \) from the input, constructs a dynamic programming array `dp` of size \( m + 1 \), and prints the sum of all elements in `dp` after filling it based on the values of \( a \) and \( b \).

