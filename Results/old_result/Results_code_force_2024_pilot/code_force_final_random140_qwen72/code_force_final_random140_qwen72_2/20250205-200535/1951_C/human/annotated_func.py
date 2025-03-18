#State of the program right berfore the function call: n is a positive integer representing the number of sale days, m is a positive integer representing the maximum number of tickets purchasable each day, k is a positive integer representing the total number of tickets to buy, and prices is a list of n positive integers where each element represents the price per ticket for each of the upcoming n days. Additionally, 1 <= n <= 3 * 10^5, 1 <= m <= 10^9, and 1 <= k <= min(n * m, 10^9).
def func_1(n, m, k, prices):
    """Calculates the minimum spending to purchase k tickets.

    Args:
        n: The number of sale days.
        m: The maximum number of tickets purchasable each day.
        k: The total number of tickets to buy.
        prices: A list of prices per ticket for each day.

    Returns:
        The minimum amount of money needed to purchase k tickets.
    """
    total_cost = 0
    tickets_bought = 0
    prices.sort()
    for i in range(n):
        tickets_to_buy = min(m, k - tickets_bought)
        
        cost = tickets_to_buy * prices[i]
        
        total_cost += cost
        
        tickets_bought += tickets_to_buy
        
        if tickets_bought == k:
            break
        
    #State: `n` remains a positive integer, `i` is `n-1` if the loop completes without breaking early, `m` remains a positive integer, `k` remains a positive integer, `prices` remains a sorted list of `n` positive integers, `total_cost` is the sum of the costs of buying the required number of tickets at the lowest possible prices, `tickets_bought` is `k` (the total number of tickets to buy), `tickets_to_buy` is 0 (since all tickets have been bought).
    return total_cost
    #The program returns the total cost, which is the sum of the costs of buying `k` tickets at the lowest possible prices from the sorted list `prices`.
#Overall this is what the function does:The function `func_1` accepts four parameters: `n` (the number of sale days), `m` (the maximum number of tickets purchasable each day), `k` (the total number of tickets to buy), and `prices` (a list of prices per ticket for each day). It calculates and returns the minimum amount of money needed to purchase `k` tickets by buying them at the lowest available prices over the given days. After the function executes, `n`, `m`, and `k` remain unchanged, while `prices` is sorted in non-decreasing order. The function ensures that the total cost reflects the optimal strategy of purchasing tickets at the lowest prices first.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, n, m, and k are positive integers such that 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9). prices is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9.
def func_2():
    """Handles input and output for multiple test cases."""
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        prices = list(map(int, input().split()))
        
        result = func_1(n, m, k, prices)
        
        print(result)
        
    #State: `t` is 0 or less, `_` is `t-1`, `n` is an input integer, `m` is an input integer, `k` is an input integer, `prices` is a list of integers input by the user, `result` is the value returned by `func_1(n, m, k, prices)` for the last iteration.
#Overall this is what the function does:The function `func_2` handles multiple test cases. It reads the number of test cases `t` from the input, and for each test case, it reads three integers `n`, `m`, and `k`, followed by a list of `n` integers `prices`. It then calls another function `func_1` with these parameters and prints the result. After processing all test cases, the function completes its execution. The final state of the program is that `t` test cases have been processed, and the results for each test case have been printed.

