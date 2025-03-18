#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5. The list a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n, and each integer from 1 through n appears at most twice in the list a. The sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: `dp` is a 2D list of size (n+1) x (n+1) where each element dp[i][j] represents the maximum number of cards that can be collected starting from index i with j cards in hand, given the conditions specified in the loop. The exact values depend on the input `cards`, but the structure remains as described.
    return dp[0][0]
    #The program returns the maximum number of cards that can be collected starting from index 0 with 0 cards in hand, as represented by the dp[0][0] element in the 2D list dp.
#Overall this is what the function does:The function calculates and returns the maximum number of cards that can be collected starting from index 0 with 0 cards in hand. This is determined using dynamic programming based on the input list of cards, where each element in the 2D list `dp` represents the maximum number of cards that can be collected under specific conditions.

