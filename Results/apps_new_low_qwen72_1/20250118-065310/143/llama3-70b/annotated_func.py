#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 30, L is an integer such that 1 ≤ L ≤ 10^9, and c is a list of n integers where each c_i satisfies 1 ≤ c_i ≤ 10^9.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 30\), `L` is an integer such that \(1 \leq L \leq 10^9\), `costs` is a list of `n` integers where each \(c_i\) satisfies \(1 \leq c_i \leq 10^9\), `dp` is a list of length \(L + 1\) where `dp[0]` is 0, and for \(1 \leq i \leq L\), `dp[i]` is the minimum cost to reach `i` using volumes \(2^j - 1\) for \(0 \leq j < n\). Variables `n`, `L`, and `costs` remain constant throughout the loop. The loop updates `dp[i]` for each valid volume \(2^j - 1\) where \(0 \leq j < n\) and `vol` is less than or equal to `i`.
    print(dp[L] if dp[L] != float('inf') else -1)
#Overall this is what the function does:The function reads two integers `n` and `L` from the input, followed by a list of `n` integers `costs`. It then calculates the minimum cost to reach a target volume `L` using volumes of the form \(2^j - 1\) (where \(0 \leq j < n\)), with each volume having an associated cost from the `costs` list. The function prints the minimum cost to reach the target volume `L`. If it is not possible to reach the target volume `L` with the given volumes, the function prints `-1`. The function does not return any value. The state of the program after the function concludes is that `n`, `L`, and `costs` remain unchanged, and the dynamic programming array `dp` contains the minimum costs to reach each volume from 0 to `L`.

