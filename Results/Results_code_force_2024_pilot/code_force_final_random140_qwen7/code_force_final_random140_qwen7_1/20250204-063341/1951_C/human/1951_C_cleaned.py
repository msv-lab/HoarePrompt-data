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
    return total_cost

def func_2():
    """Handles input and output for multiple test cases."""
    t = int(input())
    for _ in range(t):
        (n, m, k) = map(int, input().split())
        prices = list(map(int, input().split()))
        result = func_1(n, m, k, prices)
        print(result)
if __name__ == '__main__':
    func_2()