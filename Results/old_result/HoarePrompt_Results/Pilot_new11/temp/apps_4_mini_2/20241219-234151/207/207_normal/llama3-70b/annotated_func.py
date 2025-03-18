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
        
    #State of the program after the  for loop has been executed: `m`, `a`, `b` are positive integers such that \(1 \leq m \leq 10^9\), \(1 \leq a \leq 10^5\), \(1 \leq b \leq 10^5\). `dp` is a list where `dp[i]` represents the number of ways to reach index `i` using additions of `a` and subtractions of `b` from the starting index 0.
    print(sum(dp))
#Overall this is what the function does:The function reads three positive integers `m`, `a`, and `b` from user input, where `m` can be as large as \(10^9\) and `a` and `b` can be up to \(10^5\). It initializes a dynamic programming list `dp` with size `m + 1`, where `dp[i]` represents the number of ways to reach index `i` starting from index 0, by either adding `a` or subtracting `b`. The function iterates through the list updating the number of ways to reach each index according to the defined operations. After processing the list, it sums all the values in `dp` and prints this total, which represents the total number of ways to reach any index from 0 to `m` using the specified operations. Note that the function does not handle cases where `m` is very large since it allocates an array of size `m + 1`, which could lead to memory issues when `m` is close to its upper limit.

