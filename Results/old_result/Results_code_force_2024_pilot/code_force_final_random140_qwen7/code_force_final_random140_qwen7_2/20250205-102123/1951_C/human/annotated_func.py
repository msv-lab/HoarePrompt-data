#State of the program right berfore the function call: n is a positive integer representing the number of sale days, m is a positive integer representing the maximum number of tickets purchasable each day, k is a positive integer representing the total number of tickets to buy, and prices is a list of n positive integers where each element represents the price per ticket for each of the upcoming n days.
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
        
    #State: All tickets have been bought, `tickets_bought` equals `k`, `total_cost` is the sum of the costs calculated over all iterations, and `i` equals `n-1`.
    return total_cost
    #The program returns the total cost of buying `k` tickets, which is the sum of the costs calculated over all iterations.
#Overall this is what the function does:The function calculates the minimum amount of money needed to purchase `k` tickets over `n` sale days. It sorts the daily ticket prices, then iteratively buys tickets starting from the day with the lowest price until `k` tickets are purchased. For each day, it buys up to `m` tickets or the remaining number of tickets needed, whichever is smaller. The function returns the total cost of these purchases.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n, m, and k are positive integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(n⋅m, 10^9). prices is a list of n positive integers where 1 ≤ a_i ≤ 10^9 representing the price per ticket for each of the upcoming n days.
def func_2():
    """Handles input and output for multiple test cases."""
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        prices = list(map(int, input().split()))
        
        result = func_1(n, m, k, prices)
        
        print(result)
        
    #State: Output State: `t` must be greater than or equal to the total number of test cases submitted, `n` is an input integer for each test case, `m` is an input integer for each test case, `k` is an input integer for each test case, `prices` is a list of integers for each test case obtained from `input().split()` converted to integers, `result` is the return value of `func_1(n, m, k, prices)` for each test case.
    #
    #This means that after the loop has executed all its iterations, `t` will hold the final number of test cases submitted, and for each test case, `n`, `m`, `k`, and `prices` will contain the respective inputs for that test case. The variable `result` will contain the output of the function `func_1` for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads the values of \( n \), \( m \), \( k \), and a list of ticket prices, then calls another function `func_1` to compute a result based on these inputs. Finally, it prints the result for each test case.

