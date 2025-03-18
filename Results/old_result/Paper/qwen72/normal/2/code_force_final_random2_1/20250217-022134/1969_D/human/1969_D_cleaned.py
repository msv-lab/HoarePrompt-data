read_input = sys.stdin.readline

def func_1():
    return int(read_input())

def func_2():
    return map(int, read_input().split())

def func_3(primary_items, secondary_heap):
    total = sum((item[0] for item in secondary_heap))
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
    return total

def func_4():
    test_cases = func_1()
    for _ in range(test_cases):
        heap = []
        remaining_items = []
        (n, k) = func_2()
        prices = list(func_2())
        neg_prices = [-price for price in prices]
        bonuses = list(func_2())
        max_profit = 0
        current_profit = 0
        combined = list(zip(neg_prices, bonuses))
        combined.sort(key=lambda item: item[1])
        for _ in range(k):
            if combined:
                heapq.heappush(heap, combined.pop())
        if combined:
            current_profit = func_3(combined, heap)
        if current_profit > max_profit:
            max_profit = current_profit
        while combined:
            item = combined.pop()
            if item[0] + item[1] >= 0:
                current_profit -= item[1]
            else:
                current_profit += item[0]
            removed_item = heapq.heappushpop(heap, item)
            if removed_item:
                current_profit -= removed_item[0]
            if current_profit > max_profit:
                max_profit = current_profit
        print(max_profit)
func_4()