#State of the program right berfore the function call: m, a, and b are integers such that 1 <= m <= 10^9 and 1 <= a, b <= 10^5.
def func():
    m, a, b = map(int, input().split())
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(m + 1):
        if i + a <= m:
            dp[i + a] += dp[i]
        
        if i - b >= 0:
            dp[i] += dp[i - b]
        
    #State of the program after the  for loop has been executed: `m`, `a`, and `b` are input integers, `dp` is a list of length `m + 1` where `dp[i]` represents the number of ways to reach index `i` from 0 by either adding `a` or subtracting `b`, with `dp[0]` being 1.
    print(sum(dp))
#Overall this is what the function does:The function accepts three integer parameters `m`, `a`, and `b` through user input, where `m`, `a`, and `b` are integers such that `1 <= m <= 10^9` and `1 <= a, b <= 10^5`. It calculates the number of ways to reach different indices from 0 by either adding `a` or subtracting `b`, and then prints the total sum of these ways. The function effectively counts the combinations of adding `a` and subtracting `b` to reach all possible indices up to `m`, handling edge cases where `i + a` exceeds `m` or `i - b` is less than 0. The final state of the program includes the user-input integers `m`, `a`, and `b`, a list `dp` of length `m + 1` containing the number of ways to reach each index, and the printed sum of these ways, providing a result based on the input values.

