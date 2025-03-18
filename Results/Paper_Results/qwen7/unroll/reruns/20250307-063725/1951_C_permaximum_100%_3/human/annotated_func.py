#State of the program right berfore the function call: n is a positive integer representing the number of sale days, m is a positive integer representing the maximum amount of tickets purchasable each day, k is a positive integer representing the number of tickets to be bought at the end, and prices is a list of n positive integers where prices[i] represents the price per ticket on day i.
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
        
    #State: The state will be as follows: `pq` is an empty list (since all elements were popped), `total_cost` is the sum of the costs of buying up to `k` tickets with increasing prices, `tickets_bought` is equal to `k`, and `price_increase` is the total number of tickets bought.
    return total_cost
    #The program returns total_cost which is the sum of the costs of buying up to k tickets with increasing prices
#Overall this is what the function does:The function accepts four parameters: the number of sale days (n), the maximum amount of tickets purchasable each day (m), the number of tickets to be bought at the end (k), and a list of ticket prices over the sale days (prices). It calculates and returns the total cost of buying up to k tickets with the cost increasing each day based on the available tickets and the given prices.

