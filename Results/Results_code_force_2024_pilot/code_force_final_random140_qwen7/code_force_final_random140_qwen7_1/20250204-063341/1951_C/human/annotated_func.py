#State of the program right berfore the function call: n is a positive integer representing the number of sale days, m is a positive integer representing the maximum number of tickets purchasable each day, k is a positive integer representing the total number of tickets to buy, and prices is a list of n positive integers where each integer represents the price per ticket for each of the upcoming n days.
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
        
    #State: Output State: All tickets have been bought (`tickets_bought` equals `k`), the total cost is the sum of the costs calculated for each day until `k` tickets were purchased, `n` is the number of sale days, `m` is the maximum number of tickets purchasable each day, `k` is the total number of tickets to buy, `i` is the last index of the `prices` list that was used (i.e., `n-1`), and `prices` is a list of `n` positive integers sorted in ascending order. The loop has completed all its iterations, and `tickets_bought` equals `k`.
    #
    #In simpler terms, after all iterations of the loop have finished, all `k` tickets have been bought, the total amount spent (`total_cost`) is the sum of the cost of each batch of tickets bought on each day, and the loop has exited because `tickets_bought` equals `k`.
    return total_cost
    #The program returns the total cost of buying `k` tickets, which is the sum of the costs calculated for each day until `k` tickets were purchased.
#Overall this is what the function does:The function accepts the number of sale days `n`, the maximum number of tickets purchasable each day `m`, the total number of tickets to buy `k`, and a list of ticket prices `prices` for each day. It calculates and returns the minimum amount of money needed to purchase `k` tickets by buying them on the cheapest days first, ensuring no more than `m` tickets are bought on any single day.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 3⋅10^5, m is an integer such that 1 ≤ m ≤ 10^9, k is an integer such that 1 ≤ k ≤ min(n⋅m, 10^9), and prices is a list of n integers such that 1 ≤ a_i ≤ 10^9.
def func_2():
    """Handles input and output for multiple test cases."""
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        prices = list(map(int, input().split()))
        
        result = func_1(n, m, k, prices)
        
        print(result)
        
    #State: The loop has executed all its iterations, so `t` is now the final value it was initialized to. For each iteration, `n`, `m`, and `k` are integers assigned from the input split and converted to integers, and `prices` is a list of integers created by converting the input split into integers. The variable `result` holds the return value of `func_1(n, m, k, prices)` for each iteration, and these results are printed after each call to `func_1`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads values for \( n \), \( m \), \( k \), and a list of \( n \) integers representing prices. It then calls another function `func_1` with these values and prints the result returned by `func_1`. After processing all test cases, the function concludes with no return value.

