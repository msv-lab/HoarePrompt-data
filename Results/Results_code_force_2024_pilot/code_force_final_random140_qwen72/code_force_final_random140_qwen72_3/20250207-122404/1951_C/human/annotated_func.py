#State of the program right berfore the function call: n is a positive integer representing the number of sale days, m is a positive integer representing the maximum number of tickets purchasable each day, k is a positive integer representing the total number of tickets to buy, and prices is a list of positive integers representing the price per ticket for each day, where 1 <= n <= 3 * 10^5, 1 <= m <= 10^9, and 1 <= k <= min(n * m, 10^9).
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
        
    #State: `total_cost` is the sum of the costs of buying up to `k` tickets at the lowest available prices from the sorted `prices` list, `tickets_bought` is `k`, `prices` is sorted in ascending order, `n` is unchanged, `i` is the index where the loop stopped (either because `tickets_bought` reached `k` or the loop completed all `n` iterations), `tickets_to_buy` is the last calculated value of `min(m, k - tickets_bought)` before the loop terminated, and `cost` is the last calculated value of `tickets_to_buy * prices[i]` before the loop terminated.
    return total_cost
    #The program returns the sum of the costs of buying up to `k` tickets at the lowest available prices from the sorted `prices` list.
#Overall this is what the function does:The function `func_1` accepts four parameters: `n` (the number of sale days), `m` (the maximum number of tickets purchasable each day), `k` (the total number of tickets to buy), and `prices` (a list of prices per ticket for each day). It calculates and returns the minimum amount of money needed to purchase exactly `k` tickets by selecting the lowest available prices from the sorted `prices` list. After the function concludes, `total_cost` holds the minimum spending required to buy `k` tickets, `tickets_bought` equals `k`, and `prices` is sorted in ascending order. The original values of `n`, `m`, and `k` remain unchanged.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where 1 ≤ t ≤ 10^4. n, m, and k are positive integers where 1 ≤ n ≤ 3·10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9). prices is a list of n positive integers, each representing the price per ticket for each of the upcoming n days, where 1 ≤ prices[i] ≤ 10^9.
def func_2():
    """Handles input and output for multiple test cases."""
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        prices = list(map(int, input().split()))
        
        result = func_1(n, m, k, prices)
        
        print(result)
        
    #State: `t` is 0, `n`, `m`, and `k` are input integers, `prices` is a list of integers provided by the user, `result` is the value returned by `func_1(n, m, k, prices)` for each iteration.
#Overall this is what the function does:The function `func_2` processes multiple test cases, where each test case involves reading inputs `n`, `m`, `k`, and a list of prices. It then calls another function `func_1` with these inputs and prints the result. After processing all test cases, the function completes its execution. The final state of the program includes the printed results for each test case, and the input variables `t`, `n`, `m`, `k`, and `prices` are no longer relevant. The function itself does not return any value.

