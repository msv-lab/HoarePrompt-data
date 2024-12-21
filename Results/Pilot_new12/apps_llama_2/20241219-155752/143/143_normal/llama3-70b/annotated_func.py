#State of the program right berfore the function call: The function has access to input values where n is an integer between 1 and 30 (inclusive), L is an integer between 1 and 10^9 (inclusive), and there are n integers c_1, c_2,..., c_{n} (each between 1 and 10^9 inclusive) representing the costs of bottles of different types.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 30 (inclusive), `L` is an integer between 1 and 10^9 (inclusive), `costs` is a list of input integers, `dp` is a list of `L + 1` elements where `dp[0]` is 0 and `dp[i]` for `i > 0` is the minimum cost considering all possible volumes up to `i`, calculated using the volumes derived from `n` and costs from `costs`. If `L` is 0, `dp` remains unchanged with `dp[0]` being 0 and the rest being infinity.
    print(dp[L] if dp[L] != float('inf') else -1)
#Overall this is what the function does:The function calculates the minimum cost to fill a capacity `L` using bottles of different types with costs `c_1` to `c_n`, where each bottle type has a volume equal to `2^i - 1` for `i` ranging from 0 to `n-1`. The function takes no parameters but reads `n` and `L` from input, followed by `n` costs. It returns the minimum cost if it's possible to fill the capacity, otherwise, it returns `-1`. The input values `n` and `L` are integers between 1 and 30 (inclusive) and 1 and 10^9 (inclusive), respectively. The costs `c_1` to `c_n` are integers between 1 and 10^9 (inclusive). The function handles edge cases where `L` is 0, in which case it doesn't change the `dp` array, and where it's impossible to fill the capacity, in which case it returns `-1`. The function uses dynamic programming to calculate the minimum cost efficiently.

