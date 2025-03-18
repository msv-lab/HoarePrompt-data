def func_1(n, m, k, prices):
    import heapq
    pq = [(price, i) for (i, price) in enumerate(prices)]
    heapq.heapify(pq)
    total_cost = 0
    tickets_bought = 0
    price_increase = 0
    while tickets_bought < k:
        (price, day) = heapq.heappop(pq)
        price += price_increase
        tickets_to_buy = min(m, k - tickets_bought)
        total_cost += price * tickets_to_buy
        tickets_bought += tickets_to_buy
        price_increase += tickets_to_buy
    return total_cost
t = int(input())
for _ in range(t):
    (n, m, k) = map(int, input().split())
    prices = list(map(int, input().split()))
    result = func_1(n, m, k, prices)
    print(result)