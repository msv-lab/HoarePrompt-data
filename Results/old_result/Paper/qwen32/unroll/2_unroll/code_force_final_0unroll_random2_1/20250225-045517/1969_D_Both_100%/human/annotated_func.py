#State of the program right berfore the function call: No variables in the function signature.
def func_1():
    return int(read_input())
    #The program returns an integer value that is the result of converting the input string provided to `read_input()` to an integer.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It returns an integer value obtained by converting an input string to an integer.

#State of the program right berfore the function call: No variables are present in the function signature.
def func_2():
    return map(int, read_input().split())
    #The program returns a map object that lazily applies the `int` function to each element of the list obtained by splitting the string returned by `read_input()` on whitespace.
#Overall this is what the function does:The function `func_2` accepts no parameters and returns a map object. This map object applies the `int` function to each element of a list derived from splitting a string, which is obtained from `read_input()`, on whitespace.

#State of the program right berfore the function call: primary_items is a list of tuples where each tuple contains two integers, secondary_heap is a list of tuples where each tuple contains two integers.
def func_3(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: - `primary_items`: Remains unchanged.
    #   - `secondary_heap`: Remains unchanged.
    #   - `total`: Updated to include the sums of the tuples from `primary_items` that meet the condition.
    #
    #Given the above logic, the output state can be described as follows:
    #
    #Output State:
    return total
    #The program returns the updated value of `total`, which includes the sums of the tuples from `primary_items` that meet the condition.
#Overall this is what the function does:The function calculates and returns the sum of the sums of tuples from `primary_items` where the sum of the tuple's elements is non-negative, added to the sum of the first elements of all tuples in `secondary_heap`. Both input lists remain unchanged.

#State of the program right berfore the function call: heap is a list that will be used as a min-heap, remaining_items is an initially empty list, n is a positive integer representing the number of items, k is a non-negative integer such that 0 <= k <= n, prices is a list of n integers representing the prices for Alice, neg_prices is a list of n integers representing the negative prices for Alice, bonuses is a list of n integers representing the bonuses for Bob, max_profit is initialized to 0, current_profit is initialized to 0, combined is a list of tuples where each tuple contains a negative price and a bonus, and combined is sorted by the bonus values.
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
        
    #State: max_profit is the maximum profit achieved across all test cases. All other variables reflect the state of the last iteration.
#Overall this is what the function does:The function calculates and prints the maximum profit that can be achieved for Bob and Alice based on given prices, bonuses, and constraints. It processes multiple test cases, each involving a list of prices, bonuses, and a limit on the number of items that can be selected to maximize the profit.

