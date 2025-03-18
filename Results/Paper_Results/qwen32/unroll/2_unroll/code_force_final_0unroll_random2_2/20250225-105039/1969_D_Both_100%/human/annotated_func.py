#State of the program right berfore the function call: No variables in the function signature.
def func_1():
    return int(read_input())
    #The program returns an integer value that is the result of converting the input read by `read_input()` to an integer.
#Overall this is what the function does:The function reads an input, converts it to an integer, and returns this integer value.

#State of the program right berfore the function call: No specific variables are provided in the function signature. The function `func_2` is assumed to read input and return a map object containing integers, but the relationship between these integers and the problem variables (n, k, a_i, b_i) is not directly described in the function signature alone.
def func_2():
    return map(int, read_input().split())
    #The program returns a map object containing integers that were read from the input, split by whitespace.
#Overall this is what the function does:The function `func_2` reads a line of input from the user, splits it by whitespace, and returns a map object containing the integers from the input.

#State of the program right berfore the function call: primary_items is a list of tuples where each tuple contains two integers representing the price for Alice and the price for Bob respectively. secondary_heap is a list of tuples with the same structure as primary_items, representing items that have been added to a heap.
def func_3(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: `primary_items` remains the same, `secondary_heap` remains the same, `total` is the sum of its initial value and the sum of `item[0] + item[1]` for all `item` in `primary_items` where `item[0] + item[1] >= 0`.
    return total
    #The program returns the sum of the initial value of `total` and the sum of `item[0] + item[1]` for all `item` in `primary_items` where `item[0] + item[1] >= 0`.
#Overall this is what the function does:The function calculates and returns the sum of the initial value of `total` (which is the sum of the first elements of the tuples in `secondary_heap`) and the sum of the sums of the elements in each tuple from `primary_items` where the sum of the elements in the tuple is greater than or equal to zero. The input lists `primary_items` and `secondary_heap` remain unchanged.

#State of the program right berfore the function call: heap is an empty list, remaining_items is an empty list, n is a positive integer representing the number of items, k is a non-negative integer such that 0 <= k <= n, prices is a list of n integers representing the prices for Alice, neg_prices is a list of n integers representing the negative prices for Alice, bonuses is a list of n integers representing the bonuses for Bob, max_profit is initialized to 0, current_profit is initialized to 0, combined is a list of tuples where each tuple contains a negative price and a bonus, and combined is sorted based on the bonus values.
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
        
    #State: heap is an empty list, remaining_items is an empty list, n is the value returned by the last call to func_2(), k is the value returned by the last call to func_2(), prices is the list returned by the last call to func_2(), neg_prices is the list of negative values of the last prices list, bonuses is the list returned by the last call to func_2(), max_profit is the maximum profit calculated in the last iteration, current_profit is the current profit calculated in the last iteration, combined is an empty list, test_cases is the value of test_cases at the start of the loop.
#Overall this is what the function does:The function `func_4` processes multiple test cases to determine the maximum profit Alice can achieve by selecting items based on their negative prices and bonuses, while considering a limit `k` on the number of items she can initially select. It prints the maximum profit for each test case.

