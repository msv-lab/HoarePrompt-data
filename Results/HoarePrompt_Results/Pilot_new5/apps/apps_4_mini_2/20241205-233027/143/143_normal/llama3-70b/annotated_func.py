#State of the program right berfore the function call: n is an integer between 1 and 30, L is an integer between 1 and 10^9, and c is a list of n integers where each integer is between 1 and 10^9.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 30, `L` is an integer between 1 and 10^9, `c` is a list of `n` integers between 1 and 10^9, `costs` is a list of integers derived from the input provided, `dp` is a list of length `L + 1` with `dp[0]` equal to 0, `dp[i]` is the minimum cost to achieve a volume of `i` for all `i` in the range `[1, L]` considering the available volumes defined by `vol`, which are `2^j - 1` for `j` in the range `[0, n-1]`. If no valid volumes can be used to achieve a certain volume, `dp[i]` remains unchanged from its initial state of float('inf').
    print(dp[L] if dp[L] != float('inf') else -1)
#Overall this is what the function does:The function accepts two integers `n` (between 1 and 30) and `L` (between 1 and 10^9), along with a list of `n` integers representing costs. It calculates the minimum cost to achieve a volume of `L` using available volumes defined by the formula `2^j - 1` for `j` in the range from 0 to `n-1`. If it is not possible to achieve the desired volume, the function returns -1.

