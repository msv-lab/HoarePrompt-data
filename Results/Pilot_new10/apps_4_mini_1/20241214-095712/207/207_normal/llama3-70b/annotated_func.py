#State of the program right berfore the function call: m is a positive integer such that 1 <= m <= 10^9, and a and b are positive integers such that 1 <= a, b <= 10^5.
def func():
    m, a, b = map(int, input().split())
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(m + 1):
        if i + a <= m:
            dp[i + a] += dp[i]
        
        if i - b >= 0:
            dp[i] += dp[i - b]
        
    #State of the program after the  for loop has been executed: `m`, `a`, `b` are positive integers. `dp` is an array where `dp[i]` contains the number of ways to reach the index `i` using steps of size `a` and `b`, such that `dp[0]` is 1 and all other values depend on the accumulated values from previous iterations. If `i + a` is less than or equal to `m`, `dp[i + a]` is incremented by `dp[i]`, and if `i - b` is greater than or equal to 0, `dp[i]` is incremented by `dp[i - b]`. Therefore, after all iterations, `dp` reflects all possible combinations of moves to reach each index up to `m`.
    print(sum(dp))
#Overall this is what the function does:The function accepts three positive integers `m`, `a`, and `b` through user input and calculates the total number of ways to reach the index `m` using steps of size `a` (forward) and `b` (backward). It uses dynamic programming to keep track of the number of ways to reach each index from 0 to `m`. Ultimately, it prints the sum of all ways to reach each index, including those that might not be reachable with the specified `a` and `b`. If `m` is too large or `a` and `b` are outside the defined ranges, the function may not behave correctly, but this is dependent on the input constraints.

