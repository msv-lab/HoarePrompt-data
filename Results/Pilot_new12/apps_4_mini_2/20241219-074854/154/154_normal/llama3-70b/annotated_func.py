#State of the program right berfore the function call: n is an integer between 1 and 45 inclusive, k is an integer between 1 and 45 inclusive, M is a non-negative integer less than or equal to 2·10^9, and t is a list of k integers where each integer is between 1 and 1,000,000.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 45 inclusive, `k` is an integer between 1 and 45 inclusive, `M` is at least 1, `t` is a sorted list of `k` integers ranging from 1 to 1,000,000, `dp[k][1...M]` contains the maximum number of items that can be chosen for capacities ranging from 1 to `M` using all `k` items, where `dp[i][j]` represents the maximum number of items that can be chosen with the first `i` items and a total capacity of `j`.
    print(sum(dp[i][M] for i in range(k + 1)) + sum(1 for i in range(k + 1) if 
    dp[i][M] == i))
#Overall this is what the function does:The function processes inputs regarding a maximum item selection problem, where it receives an integer `n`, an integer `k`, a non-negative integer `M`, and a list `t` of `k` integers. It computes a dynamic programming table `dp` that tracks the maximum number of items that can be selected given a maximum weight capacity from `1` to `M`. After populating the table, it prints the sum of selected items for the full capacity `M` as well as the count of exact full selections that equal the total number of items selected. The function does not return values; it only prints results, and it assumes valid input as described, but does not handle cases where the inputs may be out of bounds or invalid.

