#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 30, L is a positive integer such that 1 ≤ L ≤ 10^9, and c is a list of n integers where each integer c[i] satisfies 1 ≤ c[i] ≤ 10^9.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 30, `L` is a positive integer such that 1 ≤ `L` ≤ 10^9, `c` is a list of `n` integers where each integer `c[i]` satisfies 1 ≤ `c[i]` ≤ 10^9, `costs` is a list of `n` integers where each `costs[i]` satisfies 1 ≤ `costs[i]` ≤ 10^9, `dp[0]` is 0, and for all `i` from 1 to `L`, `dp[i]` contains the minimum cost to achieve the volume `i` based on the available volumes derived from `vol = 2^j - 1` for `j` in the range from `0` to `n - 1`. If no valid volume was found for a particular `i`, then `dp[i]` remains float('inf').
    print(dp[L] if dp[L] != float('inf') else -1)
#Overall this is what the function does:The function accepts input values for `n` (the number of different costs) and `L` (the required volume). It also reads a list of costs corresponding to different volumes represented as `2^j - 1` for `j` ranging from `0` to `n-1`. The function calculates the minimum cost to achieve the volume `L`, returning the minimum cost if it exists or -1 if it is not possible to achieve that volume. It handles the case where no valid solution exists, indicated by `dp[L]` remaining as infinity, at which point it returns -1.

