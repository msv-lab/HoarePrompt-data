#State of the program right berfore the function call: No variables in the function signature.
def func_1():
    return int(read_input())
    #The program returns the integer value of the input provided by `read_input()`
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns the integer value of the input provided by `read_input()`.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2()`. The function does not take any parameters and thus has no preconditions related to input variables.
def func_2():
    return map(int, read_input().split())
    #The program returns a map object that applies the `int` function to each element of the list obtained by splitting the string returned by `read_input()`.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads input, splits it into a list of substrings, converts each substring to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: primary_items is a list of tuples where each tuple contains two integers representing the item price for Alice and Bob respectively. secondary_heap is a list of tuples with the same structure as primary_items, representing items that are already in a heap structure.
def func_3(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: The `total` is the initial sum of the first elements of the tuples in `secondary_heap` plus the sum of the sums of the elements of each tuple in `primary_items` where the sum of the elements of the tuple is non-negative. The `primary_items` and `secondary_heap` remain unchanged.
    return total
    #The program returns the total, which is the sum of the first elements of the tuples in `secondary_heap` plus the sum of the sums of the elements of each tuple in `primary_items` where the sum of the elements of the tuple is non-negative.
#Overall this is what the function does:The function calculates and returns a total, which is the sum of the first elements of the tuples in `secondary_heap` plus the sum of the sums of the elements of each tuple in `primary_items` where the sum of the elements of the tuple is non-negative. The input lists `primary_items` and `secondary_heap` remain unchanged.

#State of the program right berfore the function call: heap is a list used as a min-heap, remaining_items is a list (initially empty in the context provided), n is a positive integer representing the number of items, k is a non-negative integer such that 0 <= k <= n, prices is a list of integers representing the prices of items for Alice, neg_prices is a list of integers representing the negative prices of items for Alice, bonuses is a list of integers representing the bonuses Alice gets from selling items to Bob, max_profit is an integer representing the maximum profit Alice can achieve, current_profit is an integer representing the current profit Alice has, combined is a list of tuples where each tuple contains the negative price and the bonus of an item, and combined is sorted based on the bonus values.
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
        
    #State: `heap` is an empty list, `remaining_items` is an empty list, `n` and `k` are the values returned by `func_2()` from the last iteration, `prices` is the list returned by `func_2()` from the last iteration, `neg_prices` is a list of integers where each integer is the negative of the corresponding integer in `prices` from the last iteration, `bonuses` is the list returned by `func_2()` from the last iteration, `test_cases` is 0, `combined` is an empty list, `item` is undefined (since the loop has finished), `removed_item` is undefined (since the loop has finished), `current_profit` is adjusted based on the items pushed and popped from the heap during the last iteration, and `max_profit` is the maximum value of `current_profit` encountered during all iterations.
#Overall this is what the function does:The function calculates and prints the maximum profit Alice can achieve by selling items to Bob, considering the constraints and relationships provided. It processes multiple test cases, each involving a list of item prices, corresponding bonuses, and a limit on the number of items Alice can initially select for a special offer.

