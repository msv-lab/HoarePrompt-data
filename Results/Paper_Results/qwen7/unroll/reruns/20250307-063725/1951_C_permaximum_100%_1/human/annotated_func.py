#State of the program right berfore the function call: n is a positive integer representing the number of sale days, m is a positive integer representing the maximum amount of tickets purchasable each day, k is a positive integer representing the number of tickets to be bought at the end, and prices is a list of n positive integers representing the price per ticket for each of the upcoming n days.
def func_1(n, m, k, prices):
    pq = [(price, i) for i, price in enumerate(prices)]
    heapq.heapify(pq)
    total_cost = 0
    tickets_bought = 0
    price_increase = 0
    while tickets_bought < k:
        price, day = heapq.heappop(pq)
        
        price += price_increase
        
        tickets_to_buy = min(m, k - tickets_bought)
        
        total_cost += price * tickets_to_buy
        
        tickets_bought += tickets_to_buy
        
        price_increase += tickets_to_buy
        
    #State: tickets_bought is k, total_cost is the sum of prices for buying k tickets considering the price increase per iteration, pq is empty, n remains unchanged, m remains unchanged, k remains unchanged, price_increase is k
    return total_cost
    #The program returns total_cost which is the sum of prices for buying k tickets, with the price increasing by k for each subsequent ticket.
#Overall this is what the function does:The function accepts four parameters: `n` (the number of sale days), `m` (the maximum number of tickets purchasable each day), `k` (the number of tickets to be bought), and `prices` (a list of ticket prices for each day). It calculates and returns the total cost of buying `k` tickets, with the price increasing by `k` for each subsequent ticket. The function uses a priority queue to manage the ticket prices and ensures that no more than `m` tickets are bought on any given day.

