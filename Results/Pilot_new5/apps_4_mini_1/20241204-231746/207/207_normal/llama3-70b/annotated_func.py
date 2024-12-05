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
        
    #State of the program after the  for loop has been executed: `m` is a positive integer within the range 1 to 10^9, `a` is a positive integer within the range 1 to 10^5, `b` is a positive integer within the range 1 to 10^5, `dp` is a list where `dp[0]` is 1 and `dp[1]` to `dp[m]` are updated based on the transitions defined by adding `dp[i]` from the indices `i + a` and `i - b` as long as they fall within the valid range, `i` will range from 0 to `m`.
    print(sum(dp))
#Overall this is what the function does:The function accepts three positive integers `m`, `a`, and `b`, where `1 <= m <= 10^9` and `1 <= a, b <= 10^5`. It calculates the number of ways to reach a total of `m` using increments of `a` and decrements of `b`, and returns the sum of all valid combinations stored in the `dp` list. However, due to the constraint on `m`, the function may run into performance issues or memory limitations when `m` is large, as it tries to create a list of size `m + 1`.

