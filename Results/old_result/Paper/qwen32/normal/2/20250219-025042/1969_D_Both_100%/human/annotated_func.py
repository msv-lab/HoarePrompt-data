#State of the program right berfore the function call: No variables in the function signature. This function does not have any parameters and thus no preconditions can be derived from the signature alone.
def func_1():
    return int(read_input())
    #The program returns an integer value that is the result of converting the input read by `read_input()` to an integer.
#Overall this is what the function does:The function `func_1` reads an input, converts it to an integer, and returns this integer value.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`.
def func_2():
    return map(int, read_input().split())
    #The program returns a map object that applies the int function to each element of the list obtained by splitting the string returned from read_input().
#Overall this is what the function does:The function `func_2` takes no input parameters and returns a map object. This map object contains integers, which are derived by converting each element of a list. The list is created by splitting a string obtained from the `read_input()` function.

#State of the program right berfore the function call: primary_items is a list of tuples where each tuple contains two integers representing the price of an item for Alice and Bob respectively. secondary_heap is a list of tuples with the same structure as primary_items, representing items that have been considered and possibly optimized for in a previous step.
def func_3(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: primary_items
    return total
    #The program returns the value of `total`.
#Overall this is what the function does:The function calculates and returns the total value by summing up the prices of items from both `primary_items` and `secondary_heap`, considering only those items from `primary_items` where the sum of the prices for Alice and Bob is non-negative.

#State of the program right berfore the function call: heap is a list that will be used as a min-heap, remaining_items is a list that may store items not yet processed, n is an integer representing the number of items, k is an integer representing the number of items Bob can take for free, prices is a list of integers representing the prices of items for Alice, neg_prices is a list of integers representing the negative prices of items for Alice, bonuses is a list of integers representing the bonuses Alice receives from selling items to Bob, max_profit is an integer representing the maximum profit Alice can achieve, current_profit is an integer representing the current profit Alice has, combined is a list of tuples where each tuple contains the negative price and bonus of an item.
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
        
    #State: heap is an empty list; k is the number of items Bob can take for free; n is the number of items from the last test case; prices is the list of prices from the last test case; neg_prices is a list of integers where each integer is the negative of the corresponding integer in prices from the last test case; bonuses is the list of bonuses from the last test case; remaining_items is an empty list; test_cases is 0; combined is an empty list; current_profit reflects the net profit after processing all items from the last test case; max_profit holds the maximum profit encountered across all test cases.
#Overall this is what the function does:The function calculates and prints the maximum profit Alice can achieve by selling items to Bob, considering the prices of the items, the bonuses Alice receives, and the fact that Bob can take up to `k` items for free. It processes multiple test cases, each with its own set of items, prices, and bonuses, and outputs the maximum profit for each test case.

