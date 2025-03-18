#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a is a list of n integers such that 1 ≤ a_i ≤ 10^9, and b is a list of n integers such that 1 ≤ b_i ≤ 10^9.
def func_1():
    return int(read_input())
    #The program returns an integer 't' that is between 1 and 10^4 inclusive.
#Overall this is what the function does:The function reads an integer 't' from input, where 1 ≤ t ≤ 10^4. It then processes additional inputs including 'n', 'k', 'a', and 'b' based on specified constraints but ultimately returns the integer 't'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a and b are lists of integers such that for all i, 1 ≤ a_i ≤ 10^9 and 1 ≤ b_i ≤ 10^9.
def func_2():
    return map(int, read_input().split())
    #The program returns a map object containing integers split from the input string. The input string is obtained from read_input() which is not defined here but assumed to be a function that reads input from the user or another source.
#Overall this is what the function does:The function accepts no parameters and returns a map object containing integers split from the input string. This input string is read from an unspecified source through the `read_input()` function.

#State of the program right berfore the function call: primary_items is a list of tuples, where each tuple contains two integers (a_i, b_i). secondary_heap is a list of tuples, where each tuple also contains two integers (a_i, b_i).
def func_3(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: Postcondition: `total` is the sum of the first elements of all tuples in `secondary_heap`. For each tuple `item` in `primary_items`, if the sum of the first and second elements of `item` is greater than or equal to 0, `total` is updated to include `item[0] + item[1]`. If the sum of the first and second elements of `item` is less than 0, `total` remains unchanged.
    return total
    #The program returns the sum of the first elements of all tuples in `secondary_heap`, and for each tuple `item` in `primary_items`, if the sum of the first and second elements of `item` is greater than or equal to 0, `total` includes `item[0] + item[1]`; otherwise, `total` remains unchanged.
#Overall this is what the function does:The function accepts two parameters: `primary_items`, a list of tuples where each tuple contains two integers, and `secondary_heap`, a list of tuples where each tuple also contains two integers. It calculates the sum of the first elements of all tuples in `secondary_heap`. Additionally, for each tuple `item` in `primary_items`, if the sum of the first and second elements of `item` is greater than or equal to 0, it adds `item[0] + item[1]` to the total sum; otherwise, it does not add anything. The function returns the final calculated total.

#State of the program right berfore the function call: test_cases is a positive integer indicating the number of test cases. For each test case, n and k are positive integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= n. prices is a list of n integers where 1 <= price_i <= 10^9, and bonuses is a list of n integers where 1 <= bonus_i <= 10^9. The sum of n across all test cases does not exceed 2 * 10^5.
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
        
    #State: Output State: After the loop executes all iterations, `combined` will be an empty list, `k` will be less than or equal to 0, and `heap` will contain the last item from `combined` after all items have been processed. `current_profit` will reflect the final profit calculated after all conditions in the loop were considered, and `max_profit` will hold the highest profit achieved during the entire loop execution. The `remaining_items` list will remain empty, `neg_prices` will be a list of negative values from `prices`, `n` will be the return value of `func_2()`, and `bonuses` will be a list returned by `func_2()`.
    #
    #In simpler terms, after the loop has completed all its iterations:
    #- `combined` is empty because all items have been processed.
    #- `k` is non-positive (less than or equal to 0) because it is decremented with each iteration and starts at a positive value.
    #- `heap` contains the last item from `combined` after all processing.
    #- `current_profit` is the final profit calculated after all operations within the loop.
    #- `max_profit` is the highest profit achieved during the loop's execution.
    #- `remaining_items` is empty as it was initially.
    #- `neg_prices`, `n`, and `bonuses` remain unchanged as they are not affected by the loop.
    #- `heap` is updated after each iteration with push and pop operations.
#Overall this is what the function does:The function processes multiple test cases, each defined by parameters \( n \), \( k \), `prices`, and `bonuses`. For each test case, it calculates the maximum profit by combining elements from `prices` and `bonuses` under certain conditions. It uses a heap to manage these combinations efficiently and updates the maximum profit accordingly. After processing all test cases, it prints the highest profit achieved across all cases.

