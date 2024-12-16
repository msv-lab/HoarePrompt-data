#State of the program right berfore the function call: n, k, and M are integers such that 1 ≤ n ≤ 45, 1 ≤ k ≤ 45, and 0 ≤ M ≤ 2·10^9. The second line of input contains k integers t_{j}, where 1 ≤ t_{j} ≤ 1000000.
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
        
    #State of the program after the  for loop has been executed: `i` is `k + 1`, `k` is an integer between 1 and 45, `M` is an integer between 0 and 2·10^9, `t` is a list of `k` integers in sorted order, `dp` is a 2D list of dimensions \((k + 1) \times (M + 1)\) where each element `dp[i][j]` contains the maximum value achievable by selecting elements from the list `t` up to the current index `i - 1` such that the sum does not exceed the current value of `j`.
    print(sum(dp[i][M] for i in range(k + 1)) + sum(1 for i in range(k + 1) if 
    dp[i][M] == i))
#Overall this is what the function does:The function accepts integers \( n \), \( k \), and \( M \), a sorted list of integers \( t \), and computes the sum of the maximum value achievable by selecting a subset of elements from \( t \) such that their sum does not exceed \( M \), and the count of valid selections, and prints the result.

