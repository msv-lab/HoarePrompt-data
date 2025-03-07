#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, the first line contains a single integer n (1 ≤ n ≤ 2 · 10^5) representing the number of cards each player receives. The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the integers on the cards in your hand. Each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `n` is the initial integer inputted; `cards` is the initial list of integers representing the integers on the cards in your hand; `dp` is a 2D list of size `(n+1) x (n+1)` with values updated based on the number of occurrences of each card value in `cards`.
    return dp[0][0]
    #The program returns dp[0][0]
#Overall this is what the function does:The function processes a series of test cases where each test case consists of an integer `n` and a list of `n` integers. It calculates and returns a value `dp[0][0]` which is determined based on the occurrences of each integer in the list.

