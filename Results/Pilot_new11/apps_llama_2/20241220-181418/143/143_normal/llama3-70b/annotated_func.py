#State of the program right berfore the function call: The input consists of two lines. The first line contains two integers n and L (1 ≤ n ≤ 30; 1 ≤ L ≤ 10^9), where n is the number of types of bottles in the store and L is the required amount of lemonade in liters. The second line contains n integers c_1, c_2,..., c_{n} (1 ≤ c_{i} ≤ 10^9), which represent the costs of bottles of different types, where a bottle of type i has volume 2^{i} - 1 liters.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 30 (inclusive), `L` is an integer between 1 and 10^9 (inclusive), `costs` is a list of input integers, and `dp` is a list of length `L + 1` where `dp[0]` is 0 and for each `i` from 1 to `L`, `dp[i]` is the minimum cost to achieve a total volume of `i` using volumes defined by `2
    print(dp[L] if dp[L] != float('inf') else -1)
#Overall this is what the function does:The function calculates and returns the minimum cost to produce a required amount of lemonade, in liters, using bottles of different volumes and costs. It accepts two lines of input: the first line contains two integers, `n` (the number of bottle types) and `L` (the required amount of lemonade), and the second line contains `n` integers representing the costs of each bottle type. The function returns the minimum cost to achieve the required volume of lemonade, or -1 if it's not possible to achieve the required volume with the given bottle types. The function considers all possible combinations of bottle types to find the minimum cost, taking into account the volume of each bottle type, which is calculated as 2^i - 1 liters for the i-th bottle type. If the required volume cannot be achieved with the given bottle types, the function returns -1, indicating that it's not possible to produce the required amount of lemonade with the available bottles.

