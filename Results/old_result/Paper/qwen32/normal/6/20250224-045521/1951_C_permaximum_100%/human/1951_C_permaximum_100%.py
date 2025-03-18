def min_cost_tickets(n, m, k, prices):
    # Create a priority queue to store the prices
    import heapq
    pq = [(price, i) for i, price in enumerate(prices)]
    heapq.heapify(pq)
    
    total_cost = 0
    tickets_bought = 0
    price_increase = 0
    
    while tickets_bought < k:
        # Get the cheapest ticket
        price, day = heapq.heappop(pq)
        price += price_increase
        
        # Calculate how many tickets we can buy on this day
        tickets_to_buy = min(m, k - tickets_bought)
        
        # Update total cost and tickets bought
        total_cost += price * tickets_to_buy
        tickets_bought += tickets_to_buy
        
        # Increase prices for subsequent days
        price_increase += tickets_to_buy
    
    return total_cost
 
# Read number of test cases
t = int(input())
 
for _ in range(t):
    # Read input for each test case
    n, m, k = map(int, input().split())
    prices = list(map(int, input().split()))
    
    # Calculate and print the result
    result = min_cost_tickets(n, m, k, prices)
    print(result)