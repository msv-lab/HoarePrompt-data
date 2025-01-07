#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 30, L is a positive integer such that 1 ≤ L ≤ 10^9, and c is a list of n positive integers where each integer c[i] satisfies 1 ≤ c[i] ≤ 10^9.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 30, `L` is a positive integer such that 1 ≤ `L` ≤ 10^9, `c` is a list of `n` positive integers, `costs` is a list of integers, `dp` is updated such that `dp[i]` contains the minimum cost to achieve volume `i` for all `1 ≤ i ≤ L`.
    print(dp[L] if dp[L] != float('inf') else -1)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 30) representing the number of available options, a positive integer `L` (1 ≤ L ≤ 10^9) as a target volume, and a list `costs` of `n` positive integers (1 ≤ costs[i] ≤ 10^9) representing the costs associated with each option. It calculates the minimum cost to achieve exactly volume `L` using combinations of the powers of 2 (volume options). If it is not possible to achieve volume `L`, the function returns -1.

