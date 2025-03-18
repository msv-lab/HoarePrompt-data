#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a is a list of n integers such that 1 ≤ a_i ≤ 10^9, and b is a list of n integers such that 1 ≤ b_i ≤ 10^9.
def func_1():
    return int(read_input())
    #The program returns an integer t such that 1 ≤ t ≤ 10^4.
#Overall this is what the function does:The function processes a series of test cases defined by an integer `t` (where 1 ≤ t ≤ 10^4). For each test case, it reads integers `n` and `k` (with 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n), and two lists `a` and `b` consisting of `n` integers each (where 1 ≤ a_i ≤ 10^9 and 1 ≤ b_i ≤ 10^9). After processing these inputs, the function returns an integer `t` (1 ≤ t ≤ 10^4).

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a and b are lists of integers where a_i and b_i are such that 1 ≤ a_i, b_i ≤ 10^9 for all 1 ≤ i ≤ n.
def func_2():
    return map(int, read_input().split())
    #The program returns a map object containing integers split from the input string.
#Overall this is what the function does:The function reads input data, splits it into integers, and returns a map object containing these integers.

#State of the program right berfore the function call: primary_items is a list of tuples, where each tuple contains two integers (a_i, b_i); secondary_heap is a list of integers representing the difference (b_i - a_i) for each item.
def func_3(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: The final value of `total` is the sum of the original value of `total` and the sum of `item[0] + item[1]` for every tuple in `primary_items` where `item[0] + item[1] >= 0`
    return total
    #The program returns the total which is the sum of the original value of `total` and the sum of `item[0] + item[1]` for every tuple in `primary_items` where `item[0] + item[1] >= 0
#Overall this is what the function does:The function accepts a list of tuples `primary_items` and a list of integers `secondary_heap`. It calculates the total by adding the initial sum of values in `secondary_heap` to the sum of `item[0] + item[1]` for every tuple in `primary_items` where `item[0] + item[1]` is non-negative. The function then returns this total.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n and k are positive integers such that 1 ≤ n ≤ 2 ⋅ 10^5 and 0 ≤ k ≤ n. prices is a list of n integers where 1 ≤ price_i ≤ 10^9 for Alice's prices, and bonuses is a list of n integers where 1 ≤ bonus_i ≤ 10^9 for Bob's prices.
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
        
    #State: After the loop executes all its iterations, `combined` will be an empty list, `heap` will contain exactly `k` elements which are the smallest elements from the original `combined` list (or fewer if there weren't enough elements), `current_profit` will reflect the final profit calculation based on the operations performed within the loop, and `max_profit` will hold the highest value of `current_profit` encountered during the entire execution of the loop. All other variables (`test_cases`, `remaining_items`, `neg_prices`, `prices`, `bonuses`, `n`) will remain unchanged from their initial states.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it calculates the maximum possible profit by combining Alice's prices (represented as negative values) and Bob's bonuses. It uses a min-heap to keep track of the smallest combined values and iteratively adjusts the profit based on these values. The function ultimately prints the highest profit achieved across all test cases.

