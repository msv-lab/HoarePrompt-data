#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 30, L is a positive integer such that 1 ≤ L ≤ 10^9, and c is a list of n integers representing the costs of bottles, where each cost c[i] satisfies 1 ≤ c[i] ≤ 10^9.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 30; `L` is a positive integer such that 1 ≤ `L` ≤ 10^9; `dp[i]` represents the minimum cost to achieve a length `i` for all `1 ≤ i ≤ L`, with `dp[L]` possibly being float('inf') if no valid combinations were found.
    print(dp[L] if dp[L] != float('inf') else -1)
#Overall this is what the function does:The function accepts an integer `n`, a positive integer `L`, and a list of `n` integers representing the costs of bottles. It calculates the minimum cost to achieve a total volume of `L` using the available bottle sizes, which follow the pattern of volumes being powers of 2 minus 1 (i.e., 1, 3, 7, 15, etc.). If it is not possible to achieve the volume `L`, it returns -1. This function does not handle cases where `n` or `L` might be outside their specified ranges since input constraints are assumed to be valid.

