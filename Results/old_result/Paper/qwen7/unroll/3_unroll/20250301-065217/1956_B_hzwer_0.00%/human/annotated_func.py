#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5; the list a contains n integers such that 1 ≤ a_i ≤ n and each integer from 1 through n appears in a at most 2 times.
def func_1():
    n = int(input())
    cards = list(map(int, input().split()))
    dp = [([0] * (n + 1)) for _ in range(n + 1)]
    dp[n - 1][0] = 0
    dp[n - 2][0] = 0
    for i in range(n - 3, -1, -1):
        for j in range(n - 1, -1, -1):
            if cards.count(j + 1) == 0:
                dp[i][j] = dp[i + 1][j]
            elif cards.count(j + 1) == 1:
                dp[i][j] = max(dp[i + 1][j], dp[i + 2][j - 1] + 1)
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i + 2][j - 1] + 1, dp[i + 1][j + 1])
        
    #State: Output State: dp[0][0] contains the maximum number of non-overlapping occurrences of consecutive integers that can be formed starting from index 0 in the list `cards`. All other elements in the dp table remain 0 except those potentially updated by the loop.
    return dp[0][0]
    #dp[0][0] that contains the maximum number of non-overlapping occurrences of consecutive integers that can be formed starting from index 0 in the list `cards`
#Overall this is what the function does:The function processes a predefined list `cards` containing `n` integers and calculates the maximum number of non-overlapping occurrences of consecutive integers that can be formed starting from index 0 in the list `cards`. The result, stored in `dp[0][0]`, is returned.

