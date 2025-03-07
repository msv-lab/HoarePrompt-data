#State of the program right berfore the function call: No variables are present in the function signature.
def func_1():
    return int(read_input())
    #The program returns an integer value that is the result of converting the input read by `read_input()` to an integer.
#Overall this is what the function does:The function `func_1` reads an input, converts it to an integer, and returns this integer value.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`. Therefore, no precondition can be specified based on the variables in the signature.
def func_2():
    return map(int, read_input().split())
    #The program returns a map object that applies the int function to each element of the list obtained by splitting the string returned from read_input()
#Overall this is what the function does:The function `func_2` takes no input parameters and returns a map object that converts each element of a space-separated string (obtained from `read_input()`) into an integer.

#State of the program right berfore the function call: primary_items is a list of tuples where each tuple contains two integers representing the price of an item for Alice and Bob respectively. secondary_heap is a list of tuples with the same structure as primary_items, representing items that have been moved to a secondary heap.
def func_3(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: `primary_items` is `[(5, 10), (3, -2)]`, `secondary_heap` is a list of tuples, `total` is `16`.
    return total
    #The program returns 16
#Overall this is what the function does:The function calculates and returns the total sum of prices for items in `secondary_heap` and the sum of prices for items in `primary_items` where the sum of the two prices in the tuple is non-negative.

#State of the program right berfore the function call: heap is a list representing a min-heap, remaining_items is a list of tuples, n is an integer representing the number of items, k is an integer representing the number of items Bob can take for free, prices is a list of integers representing the prices of items for Alice, neg_prices is a list of integers representing the negative prices of items for Alice, bonuses is a list of integers representing the bonuses Bob pays for items, max_profit is an integer representing the maximum profit Alice can achieve, current_profit is an integer representing the current profit Alice has, combined is a list of tuples containing neg_prices and bonuses paired together, and the combined list is sorted based on the bonus values.
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
        
    #State: heap is [], remaining_items is [], n is the last value returned by func_2(), k is the last value returned by func_2(), prices is the last list returned by func_2(), neg_prices is the list of negative prices from the last iteration, bonuses is the last list returned by func_2(), max_profit is the maximum profit encountered, current_profit is the profit from the last iteration, combined is [], test_cases is 0.
#Overall this is what the function does:The function calculates and prints the maximum profit Alice can achieve by strategically selecting items to sell, taking into account the prices of the items, the bonuses Bob pays for them, and the number of items Bob can take for free. After processing each test case, it resets its internal state and moves on to the next test case.

