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
        
    #State of the program after the  for loop has been executed: `m` is a non-negative integer, `a` is `input_a`, `b` is `input_b`, and `dp` is a list where the first element is 1 and the remaining elements are 0. For every index `i` in the range `[0, m]`, `dp[i]` contains the number of ways to reach `i` using steps of `a` and `b`.
    print(sum(dp))
#Overall this is what the function does:The function `func()` accepts three parameters: `m`, `a`, and `b`, where `m` is a non-negative integer such that \(1 \leq m \leq 10^9\), and `a` and `b` are positive integers such that \(1 \leq a, b \leq 10^5\). It calculates the number of ways to reach each value from 0 to `m` using only steps of size `a` and `b`. Specifically, it initializes a dynamic programming array `dp` where `dp[i]` represents the number of ways to reach the value `i`. The function then iterates through all possible values up to `m`, updating `dp` based on the values of `a` and `b`. Finally, the function prints the sum of all elements in `dp`, which represents the total number of ways to reach any value from 0 to `m` using steps of `a` and `b`.

