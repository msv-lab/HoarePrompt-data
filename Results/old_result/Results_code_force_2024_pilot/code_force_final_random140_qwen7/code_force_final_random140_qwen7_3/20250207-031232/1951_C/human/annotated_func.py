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
        
    #State: All tickets have been bought, `tickets_bought` equals `k`, `total_cost` is the sum of the costs calculated for each day until `tickets_bought` reached `k`, and `i` is the last index `n-1` of the `prices` list.
    return total_cost
    #The program returns the total cost of buying `k` tickets, which is the sum of the costs calculated for each day until `tickets_bought` reached `k`
#Overall this is what the function does:The function accepts four parameters: `n` (the number of sale days), `m` (the maximum number of tickets purchasable each day), `k` (the total number of tickets to buy), and `prices` (a list of `n` positive integers representing the price per ticket for each day). It sorts the prices in ascending order and then iteratively buys tickets starting from the cheapest day until `k` tickets are purchased. The function returns the total cost of these tickets.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n, m, and k are positive integers such that 1 ≤ n ≤ 3 × 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9). prices is a list of n positive integers where each integer a_i represents the price per ticket on day i, and 1 ≤ a_i ≤ 10^9.
def func_2():
    """Handles input and output for multiple test cases."""
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        prices = list(map(int, input().split()))
        
        result = func_1(n, m, k, prices)
        
        print(result)
        
    #State: Output State: `t` must be greater than or equal to the total number of test cases, `n` is an integer input, `m` is an integer input, `k` is an integer input, `prices` is a list of integers obtained from splitting the input string and converting each element to an integer, `result` is the return value of `func_1(n, m, k, prices)` for each test case.
    #
    #This means that after the loop has executed all its iterations, `t` should be at least as large as the number of test cases processed, and for each iteration, `n`, `m`, `k`, and `prices` will hold the respective values for that test case, with `result` being the output of `func_1` for those inputs.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads the number of days (`n`), the maximum number of tickets (`m`), the maximum total price (`k`), and a list of ticket prices (`prices`). It then calls another function `func_1` with these parameters and prints the result returned by `func_1`. After processing all test cases, the function ensures that the number of test cases (`t`) is at least as many as the test cases processed, and for each test case, it correctly handles the inputs `n`, `m`, `k`, and `prices`, producing a result from `func_1` for each.

