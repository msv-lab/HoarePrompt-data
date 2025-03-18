#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a is a list of n integers such that 1 ≤ a_i ≤ 10^9. b is a list of n integers such that 1 ≤ b_i ≤ 10^9.
def func_1():
    return int(read_input())
    #The program returns an integer read from input, which is within the range 1 ≤ t ≤ 10^4.
#Overall this is what the function does:The function reads an integer from the input within the range 1 ≤ t ≤ 10^4 and returns it. This integer represents the number of test cases to follow.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a is a list of n integers such that 1 ≤ a_i ≤ 10^9. b is a list of n integers such that 1 ≤ b_i ≤ 10^9.
def func_2():
    return map(int, read_input().split())
    #The program returns a map object containing integers split from the input string.
#Overall this is what the function does:The function reads a single line of space-separated integers from the input, converts each integer to a string, and returns a map object containing these integers.

#State of the program right berfore the function call: primary_items is a list of tuples, where each tuple contains two integers (a_i, b_i); secondary_heap is a list of integers representing the difference (b_i - a_i) for each item.
def func_3(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: Output State: `primary_items` is a list of tuples, where each tuple contains two integers (a_i, b_i); `secondary_heap` is a list of integers representing the difference (b_i - a_i) for each item; `total` is the sum of the first element plus the second element of each tuple in `primary_items` if the sum of the elements in the tuple is greater than or equal to 0.
    return total
    #The program returns the sum of the first element plus the second element of each tuple in `primary_items` if the sum of the elements in the tuple is greater than or equal to 0.
#Overall this is what the function does:The function accepts a list of tuples `primary_items`, where each tuple contains two integers (a_i, b_i), and a list of integers `secondary_heap` representing the difference (b_i - a_i) for each item. It calculates and returns the sum of the first element plus the second element of each tuple in `primary_items` if the sum of the elements in the tuple is greater than or equal to 0.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases; n and k are positive integers such that 1 ≤ n ≤ 2 \cdot 10^5 and 0 ≤ k ≤ n; prices is a list of n integers where each integer represents the price a_i for Alice; bonuses is a list of n integers where each integer represents the price b_i for Bob; the sum of n across all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: max_profit is the highest profit calculated after processing all test cases according to the given logic.
#Overall this is what the function does:The function processes multiple test cases, each defined by the number of items \(n\), the number of operations \(k\), a list of item prices for Alice, and a list of item bonuses for Bob. For each test case, it calculates the maximum possible profit by strategically choosing items to buy and sell based on their prices and bonuses. The function returns the highest profit achieved across all test cases.

