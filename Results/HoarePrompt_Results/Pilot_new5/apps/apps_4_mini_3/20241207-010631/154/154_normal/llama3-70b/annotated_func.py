#State of the program right berfore the function call: n is an integer between 1 and 45 inclusive, k is an integer between 1 and 45 inclusive, M is a non-negative integer such that 0 <= M <= 2·10^9, and t is a list of k integers where each integer t[j] is between 1 and 1,000,000 inclusive.
def func():
    n, k, M = map(int, input().split())
    t = list(map(int, input().split()))
    t.sort()
    dp = [([0] * (M + 1)) for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, M + 1):
            dp[i][j] = dp[i][j - 1]
            if j >= t[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - t[i - 1]] + 1)
        
    #State of the program after the  for loop has been executed: `n` is between 1 and 45, `k` is between 1 and 45, `M` is at least 0, `t` is a sorted list of integers, and `dp[k][j]` contains the maximum number of items that can be selected from the first `k` items with a total weight not exceeding `j` for all `j` from 0 to `M`. If `M` is 0, `dp` remains initialized with 0s.
    print(sum(dp[i][M] for i in range(k + 1)) + sum(1 for i in range(k + 1) if 
    dp[i][M] == i))
#Overall this is what the function does:The function accepts three parameters: `n` (an integer between 1 and 45), `k` (an integer between 1 and 45), and `M` (a non-negative integer between 0 and 2·10^9), as well as a list `t` containing `k` integers, each between 1 and 1,000,000. It calculates the maximum number of items that can be selected from the first `k` items such that their total weight does not exceed `M`, and it prints the sum of the maximum items along with the count of configurations where the total weight equals `M`. The function does not handle cases where `M` is smaller than the smallest item in `t` explicitly, which may result in 0 items being selected.

