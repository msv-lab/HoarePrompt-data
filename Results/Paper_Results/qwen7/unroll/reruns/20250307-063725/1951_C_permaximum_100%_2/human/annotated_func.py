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
        
    #State: The total_cost is the sum of the cost of buying `k` tickets over the sale days, with the price increasing each day based on the number of tickets bought. The tickets_bought equals `k`, and the price_increase reflects the cumulative increase in price due to the number of tickets bought each day.
    return total_cost
    #The program returns the total cost of buying k tickets over the sale days, with the price increasing each day based on the number of tickets bought.
#Overall this is what the function does:The function accepts four parameters: the number of sale days (`n`), the maximum amount of tickets purchasable each day (`m`), the number of tickets to be bought at the end (`k`), and a list of ticket prices for each day (`prices`). It calculates and returns the total cost of buying `k` tickets over the sale days, with the price increasing each day based on the number of tickets bought.

