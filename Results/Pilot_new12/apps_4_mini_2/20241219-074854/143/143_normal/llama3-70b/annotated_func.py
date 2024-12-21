#State of the program right berfore the function call: n is an integer between 1 and 30 (inclusive), L is a positive integer less than or equal to 10^9, and c is a list of n integers where each c_i is between 1 and 10^9 (inclusive).
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 30, `L` is a positive integer; `dp` is a list where each index `i` from 0 to `L` potentially contains the minimum cost to achieve volume `i` considering all possible volumes derived from the `c` list; if no valid volumes are found for an index, it will remain at `float('inf')`.
    print(dp[L] if dp[L] != float('inf') else -1)
#Overall this is what the function does:The function reads two integers, `n` (the number of cost elements) and `L` (the target volume), followed by a list of `n` integers representing costs. It computes the minimum cost to achieve the exact volume `L` using combinations of powers of 2 derived from a starting index of 0 up to `n-1`. Each corresponding cost from the list can be added only if the power of 2 (computed as `2

