#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and the list of integers a_1, a_2, ..., a_n represents the integers on the cards in your hand, where each integer from 1 through n appears at most twice.
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
        
    #State: Output State: dp[0][0] is the maximum value obtained by the given logic, considering the constraints and operations within the loop.
    return dp[0][0]
    #dp[0][0], which is the maximum value obtained by the given logic, considering the constraints and operations within the loop.
#Overall this is what the function does:The function calculates and returns the maximum value obtained by a given logic involving dynamic programming. This logic iterates over a list of integers, considering specific constraints on the values of `t` and `n`. The function does not accept any parameters directly but uses input values for `n` and a list of integers `cards`. It constructs a dynamic programming table `dp` to find the maximum value based on the count of each integer in the list and updates this table in reverse order. The final result, stored in `dp[0][0]`, represents the maximum value achievable under the given conditions.

