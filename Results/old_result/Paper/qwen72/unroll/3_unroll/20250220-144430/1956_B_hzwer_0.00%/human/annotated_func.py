#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. cases is a list of tuples, where each tuple contains an integer n (1 ≤ n ≤ 2 · 10^5) and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n), representing the number of cards each player receives and the integers on the cards in your hand, respectively. Each integer from 1 to n appears in the list a_1, a_2, ..., a_n at most 2 times. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The `dp` table is updated such that `dp[i][j]` contains the maximum number of pairs that can be formed from the `i`-th card to the `n-1`-th card, given that the card with value `j+1` can be used up to its count in the `cards` list. The values of `t`, `cases`, `n`, and `cards` remain unchanged.
    return dp[0][0]
    #The program returns the maximum number of pairs that can be formed from the 0-th card to the n-1-th card, given that the card with value 1 can be used up to its count in the `cards` list.
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of integers `cards` from the input. It then computes and returns the maximum number of pairs that can be formed from the cards, considering the constraints that each integer from 1 to `n` appears in the list at most twice. The function does not modify the values of `t`, `cases`, `n`, or `cards`.

