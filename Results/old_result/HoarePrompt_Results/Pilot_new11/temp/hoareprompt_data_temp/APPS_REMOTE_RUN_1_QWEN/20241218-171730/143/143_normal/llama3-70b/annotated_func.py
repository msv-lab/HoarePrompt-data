#State of the program right berfore the function call: n and L are integers such that 1 ≤ n ≤ 30 and 1 ≤ L ≤ 10^9. c is a list of n integers where each c_i represents the cost of a bottle of type i, and 1 ≤ c_i ≤ 10^9.
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
        
    #State of the program after the  for loop has been executed: `costs` is a list of integers, `L` is an integer between 1 and \(10^9\), `dp` is a list of length `L + 1` where each element `dp[i]` (for `i` from 1 to `L`) is the minimum cost to achieve `i` using the given costs, `dp[0]` is 0.
    print(dp[L] if dp[L] != float('inf') else -1)
#Overall this is what the function does:The function takes two integers `n` and `L` (with 1 ≤ n ≤ 30 and 1 ≤ L ≤ 10^9), and a list `costs` of `n` integers (each 1 ≤ c_i ≤ 10^9). It then calculates the minimum cost to obtain exactly `L` liters of liquid using bottles of various volumes (2^j - 1 liters for j from 0 to n-1), where the cost of each bottle type is specified in the `costs` list. If it's possible to obtain exactly `L` liters, it returns the minimum cost; otherwise, it returns -1. The function uses dynamic programming to solve this problem efficiently. Potential edge cases include when `L` is 0, which is handled by setting `dp[0] = 0` initially. However, the function does not explicitly handle cases where no combination of bottle volumes can sum up to `L`, which is why the final check `if dp[L] != float('inf')` ensures that -1 is returned in such scenarios.

