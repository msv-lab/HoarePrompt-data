#State of the program right berfore the function call: n, m, and k are integers such that 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9). prices is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9.
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
        
    #State: `tickets_bought` is `k`, `total_cost` is the total cost of buying `k` tickets, and `price_increase` is the total number of tickets bought.
    return total_cost
    #The program returns the total cost of buying `k` tickets.
#Overall this is what the function does:The function `func_1` accepts four parameters: `n`, `m`, `k`, and `prices`. It calculates and returns the total cost of buying `k` tickets, where `n` is the number of different ticket types, `m` is the maximum number of tickets available for each type, `k` is the total number of tickets to buy, and `prices` is a list of prices for each ticket type. After the function concludes, `k` tickets have been bought, and the total cost reflects the sum of the prices of these tickets, considering that the price of each ticket type increases by the number of tickets already bought from that type.

