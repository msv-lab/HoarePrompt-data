#State of the program right berfore the function call: n and L are integers such that 1 ≤ n ≤ 30 and 1 ≤ L ≤ 10^9. c is a list of n integers where each c_i is an integer such that 1 ≤ c_i ≤ 10^9.
def func():
    n, L = map(int, input().split())
    costs = list(map(int, input().split()))
    dp = [float('inf')] * (L + 1)
    dp[0] = 0
    for i in range(1, L + 1):
        for j in range(n):
            vol = 2 ** j - 1
            if vol <= i:
                dp[i] = min(dp[i], dp[i - vol] + costs[j])
        
    #State of the program after the  for loop has been executed: `i` is `L+1`, `L` is a positive integer, `n` is a positive integer, `vol` is a positive integer that depends on `j` (where `vol` = 2^j - 1 for each iteration), `dp[i]` is the minimum cost to achieve the value `L` using the given costs, `j` is the last value of `j` used in the loop.
    print(dp[L] if dp[L] != float('inf') else -1)
#Overall this is what the function does:The function `func` accepts two integer inputs `n` and `L` (where \(1 \leq n \leq 30\) and \(1 \leq L \leq 10^9\)), and a list `costs` of `n` integers (each between 1 and \(10^9\)). It uses dynamic programming to find the minimum cost to fill a knapsack of size `L` using subsets of the given costs. If it is possible to achieve the exact size `L`, it returns the minimum cost; otherwise, it returns -1.

