#State of the program right berfore the function call: The function should accept multiple test cases. Each test case consists of an integer n (1 ≤ n ≤ 2 · 10^5) and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the cards in your hand. The integer n represents the number of cards each player receives, and each integer from 1 to n appears at most twice in the list. The total number of test cases t is given, with 1 ≤ t ≤ 10^4, and the sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: After the loop executes all iterations, `dp` is a 2D list with dimensions (n + 1) x (n + 1), where each element is initialized to 0 except for the values that have been updated by the loop. The value `dp[0][0]` will be the final result, representing the maximum number of cards that can be taken under the given conditions. The loop has processed all values of `i` from `n - 3` down to `0` and all values of `j` from `n - 1` down to `0`. For each `j` from `n - 1` down to `0`, the value `dp[i][j]` has been set based on the count of the integer `j + 1` in the `cards` list. If `j + 1` does not appear in `cards`, `dp[i][j]` is set to `dp[i + 1][j]`. If `j + 1` appears exactly once, `dp[i][j]` is set to the maximum of `dp[i + 1][j]` and `dp[i + 2][j - 1] + 1`. If `j + 1` appears at least twice, `dp[i][j]` is set to the maximum of `dp[i + 1][j]`, `dp[i + 2][j - 1] + 1`, and `dp[i + 1][j + 1]`. The total number of test cases `t` is given with 1 ≤ t ≤ 10^4, and the sum of n over all test cases does not exceed 2 · 10^5.
    return dp[0][0]
    #The program returns the maximum number of cards that can be taken under the given conditions, which is stored in `dp[0][0]`.
#Overall this is what the function does:The function `func_1` processes a single test case where it reads an integer `n` and a list of `n` integers `cards` from the input. It then computes and returns the maximum number of cards that can be taken under the given conditions, which is stored in `dp[0][0]`. The conditions are such that each integer from 1 to `n` can appear at most twice in the `cards` list. The function uses dynamic programming to determine this maximum number.

