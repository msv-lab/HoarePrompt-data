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
        
    #State of the program after the  for loop has been executed: `dp` is a list of length `m + 1` where each element `dp[i]` (0 ≤ i ≤ m) is the number of ways to reach the index `i` using the allowed operations of adding `a` and subtracting `b`, starting from `dp[0] = 1`.
    print(sum(dp))
#Overall this is what the function does:The function processes three integer inputs \(m\), \(a\), and \(b\) where \(1 \leq m \leq 10^9\), \(1 \leq a, b \leq 10^5\). It constructs a dynamic programming array `dp` of length \(m+1\) where `dp[i]` represents the number of ways to reach index `i` by either adding `a` or subtracting `b` from previous indices, starting with `dp[0] = 1`. After the for loop, the function prints the sum of all elements in `dp`, which indicates the total number of ways to reach any index up to `m` using the given operations. If `a > m` or `b > m`, the corresponding operations are not performed, and the initial `dp` values remain unchanged. If `b > m`, the subtraction operation is effectively ignored for indices less than `b`.

