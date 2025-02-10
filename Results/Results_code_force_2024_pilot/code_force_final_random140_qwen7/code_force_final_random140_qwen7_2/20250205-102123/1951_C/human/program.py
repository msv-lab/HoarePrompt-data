def min_spending(n, m, k, prices):
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
 
    # Sort the prices in ascending order
    prices.sort()
 
    # Iterate through the sorted prices
    for i in range(n):
        # Determine the maximum number of tickets to buy on this day
        tickets_to_buy = min(m, k - tickets_bought)
 
        # Calculate the cost of buying these tickets
        cost = tickets_to_buy * prices[i]
 
        # Update the total cost and number of tickets bought
        total_cost += cost
        tickets_bought += tickets_to_buy
 
        # If we have bought enough tickets, break the loop
        if tickets_bought == k:
            break
 
    return total_cost
 
 
def main():
    """Handles input and output for multiple test cases."""
 
    t = int(input())  # Read the number of test cases
 
    for _ in range(t):
        n, m, k = map(int, input().split())  # Read n, m, and k
        prices = list(map(int, input().split()))  # Read the prices
 
        # Calculate and print the minimum spending
        result = min_spending(n, m, k, prices)
        print(result)
 
 
if __name__ == "__main__":
    main()