#State of the program right berfore the function call: The function takes no parameters, but the input is provided in two lines: the first line contains two integers n and L (1 ≤ n ≤ 30; 1 ≤ L ≤ 10^9), and the second line contains n integers c_1, c_2,..., c_{n} (1 ≤ c_{i} ≤ 10^9), where n is the number of types of bottles in the store and the required amount of lemonade in liters, and c_i is the cost of a bottle of type i with volume 2^{i} - 1 liters.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 30 (inclusive), `L` is an integer between 1 and 10^9 (inclusive), `costs` is a list of `n` integers, `dp` is a list of `L + 1` elements where `dp[i]` is the minimum cost to achieve `i` using volumes up to `n`, calculated as the minimum of its original value and `dp[i - vol] + costs[j]` for all `j` where `vol = 2
    print(dp[L] if dp[L] != float('inf') else -1)
#Overall this is what the function does:The function calculates the minimum cost to make a specified amount of lemonade using bottles of different volumes and costs, and returns the minimum cost if possible, or -1 if it is impossible to make the specified amount of lemonade.

