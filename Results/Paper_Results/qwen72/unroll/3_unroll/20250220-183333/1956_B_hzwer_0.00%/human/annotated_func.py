#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), and a is a list of n integers (1 ≤ a_i ≤ n) where each integer from 1 to n appears at most twice in the list.
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
        
    #State: The `dp` table is filled from the bottom up, where `dp[i][j]` represents the maximum number of pairs that can be formed starting from index `i` in the `cards` list, with the last card used being `j+1`. The final state of `dp` will reflect the optimal solutions for all subproblems, and the value of `dp[0][0]` will be the maximum number of pairs that can be formed from the entire `cards` list. The values of `n`, `a`, and `cards` remain unchanged.
    return dp[0][0]
    #The program returns the maximum number of pairs that can be formed from the entire `cards` list, which is stored in `dp[0][0] after the `dp` table has been filled from the bottom up.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list `a` of `n` integers, where each integer from 1 to `n` appears at most twice. It returns the maximum number of pairs that can be formed from the list `a`. The values of `n` and `a` remain unchanged after the function execution.

