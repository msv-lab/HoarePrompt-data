#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a is a list of n integers such that 1 ≤ a_i ≤ 10^9, and b is a list of n integers such that 1 ≤ b_i ≤ 10^9.
def func_1():
    return int(read_input())
    #The program returns an integer t such that 1 ≤ t ≤ 10^4.
#Overall this is what the function does:The function processes a series of test cases defined by an integer t (1 ≤ t ≤ 10^4). For each test case, it reads integers n and k (1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n), and two lists a and b, each containing n integers (1 ≤ a_i ≤ 10^9 and 1 ≤ b_i ≤ 10^9). After processing these inputs, the function returns an integer t such that 1 ≤ t ≤ 10^4.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a is a list of n integers such that 1 ≤ a_i ≤ 10^9. b is a list of n integers such that 1 ≤ b_i ≤ 10^9.
def func_2():
    return map(int, read_input().split())
    #The program returns a map object containing integers split from the input string.
#Overall this is what the function does:The function reads an input string, splits it into individual elements, converts these elements to integers, and returns a map object containing these integers.

#State of the program right berfore the function call: primary_items is a list of tuples, where each tuple contains two integers (a_i, b_i). secondary_heap is a list of tuples, where each tuple also contains two integers (a_i, b_i).
def func_3(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: After all iterations of the loop, `total` will be the sum of the first elements of all tuples in `secondary_heap` plus the sum of `item[0] + item[1]` for all tuples in `primary_items` where `item[0] + item[1]` is greater than or equal to 0. The `primary_items` list will be empty since the loop processes each item exactly once.
    return total
    #The program returns the total which is the sum of the first elements of all tuples in `secondary_heap` plus the sum of `item[0] + item[1]` for all tuples in `primary_items` where `item[0] + item[1]` is greater than or equal to 0. Since `primary_items` is empty, only the sum of the first elements of all tuples in `secondary_heap` is considered.
#Overall this is what the function does:The function accepts two parameters: `primary_items`, a list of tuples where each tuple contains two integers, and `secondary_heap`, a list of tuples where each tuple also contains two integers. It calculates and returns the total sum, which is the sum of the first elements of all tuples in `secondary_heap` plus the sum of `item[0] + item[1]` for all tuples in `primary_items` where `item[0] + item[1]` is greater than or equal to 0. If `primary_items` is empty, only the sum of the first elements of all tuples in `secondary_heap` is returned.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n and k are positive integers such that 1 ≤ n ≤ 2·10^5 and 0 ≤ k ≤ n. prices is a list of n integers where each integer represents the price for Alice (a_i) and bonuses is a list of n integers where each integer represents the price for Bob (b_i).
def func_4():
    test_cases = func_1()
    for _ in range(test_cases):
        heap = []
        
        remaining_items = []
        
        n, k = func_2()
        
        prices = list(func_2())
        
        neg_prices = [(-price) for price in prices]
        
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
        
    #State: All test cases have been processed, `combined` is an empty list, `heap` contains all the items that were popped from `combined` during the iterations, `max_profit` reflects the highest profit achieved across all test cases, `k` remains 0, `remaining_items` is still an empty list, and `neg_prices` retains the list of negative prices from the `prices` list.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it calculates the maximum profit Alice can achieve by combining her prices (a_i) and Bob's prices (b_i) under certain conditions. Specifically, it uses a heap to manage a subset of these prices and iteratively adjusts the profit based on the combined values. After processing all test cases, it prints the highest profit achieved across all cases.

