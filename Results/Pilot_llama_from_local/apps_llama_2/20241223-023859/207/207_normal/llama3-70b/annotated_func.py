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
        
    #State of the program after the  for loop has been executed: `m` is an integer, `a` is the second input integer, `b` is the third input integer, `dp` is a list of length `m + 1` where `dp[i]` represents the number of ways to reach `i` by adding `a` or subtracting `b` from previous indices, with `dp[0]` being 1, and other `dp[i]` values updated accordingly based on the loop's rules.
    print(sum(dp))
#Overall this is what the function does:The function calculates and prints the total number of ways to reach all indices from 0 to `m` by either adding `a` or subtracting `b` from previous indices, where `m`, `a`, and `b` are input integers. It initializes a list `dp` of length `m + 1` to track the number of ways to reach each index, with `dp[0]` set to 1. The function then iterates over the range from 0 to `m`, updating `dp[i]` based on the rules defined in the loop. The final state of the program includes the printed sum of all values in `dp`, which represents the total number of ways to reach all indices. The function handles edge cases where `i + a` exceeds `m` and `i - b` is less than 0 by only updating `dp` when these conditions are met. The function does not return any value, and its sole output is the printed sum.

