#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5. The list of integers a_1, a_2, ..., a_n represents the integers on the cards in your hand, and each integer from 1 through n appears in the list at most 2 times. The sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: The final state of `dp[i][j]` will be the maximum value achievable for each cell based on the conditions provided in the loop.
    return dp[0][0]
    #The program returns the maximum value achievable for the cell dp[0][0] based on the conditions provided in the loop.
#Overall this is what the function does:The function processes a list of integers representing cards in a hand, where each integer from 1 through n appears at most twice. It calculates and returns the maximum value achievable for the cell dp[0][0] based on specific conditions involving dynamic programming. This value reflects the optimal strategy for selecting cards under given constraints.

