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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 30, `L` is an integer between 1 and \(10^9\), `c` is a list of `n` integers where each `c_i` is an integer between 1 and \(10^9\), `costs` is a list of `n` integers read from input, `dp` is a list of `L + 1` elements where `dp[i]` contains the minimum cost to achieve a volume of `i` using the given items.
    print(dp[L] if dp[L] != float('inf') else -1)
#Overall this is what the function does:The function accepts two inputs: an integer `n` representing the number of items, and an integer `L` representing the target volume. It also takes a list `c` of `n` integers, where each integer represents the volume capacity of an item. The function calculates the minimum cost to achieve the target volume `L` using the given items. If it is impossible to achieve the target volume, it returns -1. The function reads the values of `n`, `L`, and the list `c` from standard input. The function constructs a dynamic programming table `dp` where `dp[i]` represents the minimum cost to achieve a volume of `i`. After executing the function, the program prints the value of `dp[L]` if it is finite, otherwise, it prints -1. Potential edge cases include when `L` is 0 (where no items are needed and the cost is 0) or when the input does not conform to the specified constraints (e.g., `n` or `L` are out of bounds).

