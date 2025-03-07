#State of the program right berfore the function call: The function `func_1` takes no arguments. The input is read from standard input where the first line contains the number of test cases `t` (1 ≤ t ≤ 10^4). For each test case, the first line contains a single integer `n` (1 ≤ n ≤ 2 · 10^5) representing the number of cards each player receives. The second line contains `n` integers `a_1, a_2, ..., a_n` (1 ≤ a_i ≤ n) representing the integers on the cards in your hand. It is guaranteed that each integer from 1 through n appears in the sequence `a_1, a_2, ..., a_n` at most 2 times. The sum of `n` over all test cases does not exceed 2 · 10^5.
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
        
    #State: The `dp` table is fully updated after all iterations, with `dp[i][j]` values reflecting the maximum number of cards that can be collected based on the occurrences of each card in `cards`. Specifically, for each `i` from `0` to `n-3` and for each `j` from `0` to `n-1`, `dp[i][j]` is calculated according to the rules defined in the loop. If `cards.count(j + 1)` is 0, `dp[i][j]` is equal to `dp[i + 1][j]`. If `cards.count(j + 1)` is 1, `dp[i][j]` is `max(dp[i + 1][j], dp[i + 2][j - 1] + 1)`. Otherwise, `dp[i][j]` is the maximum of `dp[i + 1][j]`, `dp[i + 2][j - 1] + 1`, and `dp[i + 1][j + 1]`. The values of `n` and `cards` remain unchanged, and `dp` is a 2D list of size `(n + 1) x (n + 1)`. The loop has completed all iterations with `i` ranging from `n - 3` down to `0` and `j` ranging from `n - 1` down to `0`.
    return dp[0][0]
    #The program returns the value of `dp[0][0]`, which reflects the maximum number of cards that can be collected based on the occurrences of each card in the list `cards`.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a list of integers representing cards. It calculates and returns the maximum number of cards that can be collected based on the occurrences of each card in the list for each test case.

