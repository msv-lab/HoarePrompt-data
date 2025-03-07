#State of the program right berfore the function call: None
def func_1():
    return int(read_input())
    #The program returns an integer value that was input by the user.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an integer value that was input by the user. After the function concludes, the program state includes the returned integer, which represents the user's input converted to an integer.

#State of the program right berfore the function call: None of the variables are passed as arguments to the function `func_2`. This function reads input from the standard input and splits it into a list of integers.
def func_2():
    return map(int, read_input().split())
    #The program returns a map object that converts each element from the user's input (which is expected to be a space-separated string of numbers) into an integer. The exact integers depend on the user's input.
#Overall this is what the function does:The function `func_2` reads a space-separated string of numbers from the standard input and returns a map object that converts each element of the string into an integer. The returned map object contains the integers derived from the user's input.

#State of the program right berfore the function call: primary_items is a list of tuples where each tuple contains two integers representing the prices for Alice and Bob respectively, and secondary_heap is a list of tuples where each tuple contains two integers representing the prices for Alice and Bob respectively.
def func_3(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: After all iterations of the loop, `primary_items` will have been fully iterated over, and `total` will be the sum of `total` plus the sum of the first and second elements of each tuple in `primary_items` where the sum of these elements is greater than or equal to 0. The `secondary_heap` remains unchanged.
    return total
    #The program returns the final value of `total`, which is the sum of `total` plus the sum of the first and second elements of each tuple in `primary_items` where the sum of these elements is greater than or equal to 0. The `secondary_heap` remains unchanged.
#Overall this is what the function does:The function `func_3` takes two parameters: `primary_items`, a list of tuples where each tuple contains two integers representing prices for Alice and Bob, and `secondary_heap`, a list of tuples with similar structure. It calculates the sum of the first and second elements of each tuple in `secondary_heap` and adds to it the sum of the first and second elements of each tuple in `primary_items` where the sum of these elements is greater than or equal to 0. The function returns this total sum. The `secondary_heap` remains unchanged throughout the function's execution.

#State of the program right berfore the function call: test_cases is a positive integer representing the number of test cases, n and k are non-negative integers such that 0 <= k <= n, prices is a list of integers representing the prices Alice pays for the items, bonuses is a list of integers representing the prices Bob pays for the items, and both prices and bonuses have the same length n.
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
        
    #State: After the loop executes all iterations, `test_cases` is 0, `heap` is an empty list, `remaining_items` is an empty list, `n` and `k` are the values assigned from the last call to `func_2()`, `prices` is a list containing the values returned by the last call to `func_2()`, `neg_prices` is a list containing the negated values of the last `prices` list, `bonuses` is a list containing the values returned by the last call to `func_2()`, `combined` is an empty list, `current_profit` is the final calculated profit after processing all items in the last iteration, and `max_profit` is the maximum profit observed during the entire loop execution.
#Overall this is what the function does:The function `func_4` processes a series of test cases, each involving a set of items with associated prices and bonuses. For each test case, it calculates the maximum possible profit by selecting up to `k` items, considering both the negative prices (Alice's payments) and bonuses (Bob's payments). The function prints the maximum profit for each test case. After processing all test cases, the function leaves the internal state reset for the next call, with `test_cases` reduced to 0 and other internal variables cleared or reset to their initial states.

