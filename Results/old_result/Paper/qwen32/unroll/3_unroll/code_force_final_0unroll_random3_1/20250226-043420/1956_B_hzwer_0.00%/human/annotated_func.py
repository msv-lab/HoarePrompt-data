#State of the program right berfore the function call: Each test case consists of an integer n (1 ≤ n ≤ 2 · 10^5) representing the number of cards each player receives, followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the integers on the cards in your hand. It is guaranteed that each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `n` is an input integer representing the number of cards each player receives; `cards` is a list of `n` integers representing the integers on the cards in your hand; `dp` is a 2D list of dimensions `(n + 1) x (n + 1)` with values updated based on the maximum number of cards that can be collected without picking two consecutive cards of the same value.
    return dp[0][0]
    #The program returns the value of `dp[0][0]`
#Overall this is what the function does:The function takes an integer `n` and a list of `n` integers as input, representing the number of cards and the values on the cards, respectively. It calculates and returns the maximum number of cards that can be collected without picking two consecutive cards of the same value.

