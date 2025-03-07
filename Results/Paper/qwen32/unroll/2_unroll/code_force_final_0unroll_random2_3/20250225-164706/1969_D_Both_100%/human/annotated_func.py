#State of the program right berfore the function call: No variables are present in the function signature.
def func_1():
    return int(read_input())
    #The program returns an integer that is the result of converting the input read by `read_input()` to an integer.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads an input from the user, converts it to an integer, and returns that integer.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`.
def func_2():
    return map(int, read_input().split())
    #The program returns a map object that contains integers converted from the input string split by spaces.
#Overall this is what the function does:The function `func_2` takes no input parameters and returns a map object containing integers derived from splitting a predefined input string by spaces.

#State of the program right berfore the function call: primary_items is a list of tuples where each tuple contains two integers representing the price of an item for Alice and Bob respectively. secondary_heap is a list of tuples with the same structure as primary_items, representing items that have been placed in a secondary heap (likely for processing).
def func_3(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: `primary_items` is a list of tuples where each tuple contains two integers representing the price of an item for Alice and Bob respectively; `secondary_heap` is a list of tuples with the same structure as `primary_items`, representing items that have been placed in a secondary heap; `total` is the sum of the first elements of each tuple in `secondary_heap` plus the sum of the sums of the two integers in each tuple of `primary_items` where the sum of the two integers is non-negative.`
    return total
    #The program returns the total, which is the sum of the first elements of each tuple in `secondary_heap` plus the sum of the sums of the two integers in each tuple of `primary_items` where the sum of the two integers is non-negative.
#Overall this is what the function does:The function calculates and returns the total cost, which includes the sum of the first elements of each tuple in `secondary_heap` and the sum of the sums of the two integers in each tuple of `primary_items` where the sum of the two integers is non-negative.

#State of the program right berfore the function call: heap is an empty list that will be used as a min-heap, remaining_items is an empty list (its purpose is not clear from the given function), n is a positive integer representing the number of items, k is a non-negative integer such that 0 <= k <= n, prices is a list of n integers representing the prices for Alice, neg_prices is a list of n integers representing the negative prices for Alice, bonuses is a list of n integers representing the bonuses for Bob, max_profit is an integer initialized to 0, current_profit is an integer initialized to 0, combined is a list of tuples where each tuple contains a negative price and a bonus for each item, and combined is sorted based on the bonus values.
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
        
    #State: Output State: `heap` is an empty list, `remaining_items` is an empty list, `n` is the value returned by `func_2()` in the last iteration, `k` is the value returned by `func_2()` in the last iteration, `prices` is the list returned by `func_2()` in the last iteration, `neg_prices` is the list of negated prices from the last iteration, `bonuses` is the list returned by `func_2()` in the last iteration, `max_profit` is the maximum profit found across all test cases, `current_profit` is 0, `combined` is an empty list, `test_cases` is the return value of `func_1()`.
#Overall this is what the function does:The function `func_4` processes a series of test cases to determine the maximum profit that can be achieved. For each test case, it evaluates a list of items, each associated with a price and a bonus, to optimize the profit under the constraint of selecting up to `k` items. It calculates the maximum possible profit by strategically choosing items and adjusting the profit based on their prices and bonuses. The final output for each test case is the maximum profit found.

