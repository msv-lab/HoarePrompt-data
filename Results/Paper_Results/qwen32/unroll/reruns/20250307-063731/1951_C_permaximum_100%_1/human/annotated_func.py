#State of the program right berfore the function call: n is an integer such that 1 <= n <= 3 * 10^5, m is an integer such that 1 <= m <= 10^9, k is an integer such that 1 <= k <= min(n * m, 10^9), and prices is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9.
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
        
    #State: `total_cost` is the total cost of buying `k` tickets, `tickets_bought` is `k`, and `price_increase` is `k`.
    return total_cost
    #The program returns total_cost, which is the total cost of buying k tickets
#Overall this is what the function does:The function calculates the total cost of buying `k` tickets from `n` different ticket types, where each ticket type has a specific price. It ensures that no more than `m` tickets are bought from any single type and returns the total cost incurred.

