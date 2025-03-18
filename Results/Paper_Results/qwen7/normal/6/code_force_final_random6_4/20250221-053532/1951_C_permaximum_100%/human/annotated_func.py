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
        
    #State: Output State: `price_increase` is increased by the total number of tickets bought, `total_cost` is the sum of the cost of all tickets bought, `tickets_bought` equals `k`, `price` is the last price plus the final `price_increase`, `tickets_to_buy` is the minimum of `m` and `k - tickets_bought` for the last iteration, `day` is the `day` value popped from the priority queue `pq` during the last iteration.
    #
    #This means that after the loop has executed all its iterations, `price_increase` will have been incremented by the total number of tickets bought across all iterations. The `total_cost` will be the cumulative cost of all tickets purchased. `tickets_bought` will equal `k`, indicating that all available tickets have been bought. The `price` will reflect the final price after all increments. `tickets_to_buy` will be the minimum of `m` and the remaining tickets needed to reach `k` for the last iteration, and `day` will be the `day` value corresponding to the last ticket bought.
    return total_cost
    #The program returns the total cost of all tickets bought, which is the cumulative sum of the cost of each ticket purchased over all iterations.
#Overall this is what the function does:The function accepts four parameters: `n` (the number of sale days), `m` (the maximum number of tickets purchasable each day), `k` (the number of tickets to be bought), and `prices` (a list of ticket prices for each day). It calculates and returns the total cost of buying `k` tickets over `n` days, considering the price increases based on the number of tickets bought each day.

