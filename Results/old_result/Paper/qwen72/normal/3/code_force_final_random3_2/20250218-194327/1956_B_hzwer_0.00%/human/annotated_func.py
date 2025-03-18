#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. cases is a list of tuples, where each tuple contains an integer n (1 ≤ n ≤ 2 · 10^5) and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n), representing the number of cards each player receives and the integers on the cards in the player's hand, respectively. Each integer from 1 to n appears at most twice in the list a_1, a_2, ..., a_n. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop has completed all iterations, and the `dp` table is fully populated according to the rules specified in the loop. The variable `t` remains an integer representing the number of test cases where 1 ≤ t ≤ 10^4. The list `cases` remains unchanged. The integer `n` remains the input integer, and the list `cards` remains the list of integers read from the input. The variable `i` is -1, and `j` is -1.
    return dp[0][0]
    #The program returns the value stored in `dp[0][0]`, which is the result of the dynamic programming algorithm applied to the first test case and the first card in the `cards` list.
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of integers `cards` from the input. It then applies a dynamic programming algorithm to determine the maximum number of cards that can be selected from the list `cards` such that no two selected cards have the same value. The function returns this maximum number as an integer. The function does not modify the input variables or any external state.

