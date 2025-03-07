#State of the program right berfore the function call: The function `func_1()` is expected to handle multiple test cases. For each test case, `n` is an integer such that 1 ≤ n ≤ 2 · 10^5, representing the number of cards you and Nene each receive. The second line of each test case contains a list of `n` integers `a_1, a_2, ..., a_n` where each integer is between 1 and n inclusive, and each integer from 1 through n appears in the list at most 2 times. The total sum of `n` across all test cases does not exceed 2 · 10^5.
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
        
    #State: The `dp` table is fully populated, and `dp[0][0]` holds the maximum number of cards that can be collected starting from the beginning of the `cards` list.
    return dp[0][0]
    #The program returns the maximum number of cards that can be collected starting from the beginning of the `cards` list, which is stored in `dp[0][0]`.
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of `n` integers, where each integer is between 1 and `n` inclusive and appears at most twice. It calculates and returns the maximum number of cards that can be collected starting from the beginning of the list.

