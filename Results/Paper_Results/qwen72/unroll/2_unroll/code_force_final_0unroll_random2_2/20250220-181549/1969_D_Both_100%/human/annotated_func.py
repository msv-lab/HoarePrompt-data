#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_1():
    return int(read_input())
    #The program returns an integer value that is input by the user.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an integer value provided by the user. After the function concludes, the program has returned an integer value that was input by the user.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters. The function reads input from a source (presumably standard input) and splits it into integers.
def func_2():
    return map(int, read_input().split())
    #The program returns a map object that contains the integers obtained from splitting the input string.
#Overall this is what the function does:The function `func_2` reads a string from the standard input, splits it into substrings based on whitespace, converts each substring into an integer, and returns a map object containing these integers. The function does not modify any external state and does not take any parameters. After the function concludes, the map object can be iterated over to access the integers.

#State of the program right berfore the function call: primary_items is a list of tuples where each tuple contains two integers (a_i, b_i) representing the price of an item for Alice and Bob respectively, and secondary_heap is a list of tuples where each tuple contains two integers (a_i, b_i) representing the price of an item for Alice and Bob respectively.
def func_3(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: primary_items = [(1, 2), (-3, 4), (5, -6), (7, 8)], secondary_heap = [(10, 20), (30, 40)], total = 59.
    return total
    #The program returns 59.
#Overall this is what the function does:The function `func_3` takes two parameters, `primary_items` and `secondary_heap`, both of which are lists of tuples. Each tuple contains two integers representing the prices of an item for Alice and Bob. The function calculates the total sum of the first elements of the tuples in `secondary_heap` and adds to this sum the combined prices (first element + second element) of the tuples in `primary_items` where the combined price is non-negative. The function returns this total sum.

#State of the program right berfore the function call: No variables are passed in the function signature, but the function internally uses variables such as `test_cases`, `heap`, `remaining_items`, `n`, `k`, `prices`, `neg_prices`, `bonuses`, `max_profit`, `current_profit`, and `combined`. These variables are expected to be initialized and manipulated within the function, with `test_cases` being a positive integer, `n` and `k` being non-negative integers where 0 <= k <= n, `prices` and `bonuses` being lists of positive integers, and `combined` being a list of tuples where each tuple contains a negative integer and a positive integer.
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
        
    #State: The loop iterates `test_cases` times, and after each iteration, the variables `heap`, `remaining_items`, `n`, `k`, `prices`, `neg_prices`, `bonuses`, `max_profit`, `current_profit`, and `combined` are reset to their initial values within the loop. Therefore, after all iterations, these variables will not retain any specific final state from the last iteration, but the `max_profit` for each test case will be printed. The variables `test_cases` and any other variables not mentioned in the loop head and body remain unchanged.
#Overall this is what the function does:The function `func_4` does not accept any parameters. It performs a series of operations to determine and print the maximum profit that can be achieved for each of `test_cases` test cases. Each test case involves selecting `k` items from a list of `n` items, where each item has a price and a bonus. The function initializes and manipulates internal variables such as `heap`, `remaining_items`, `n`, `k`, `prices`, `neg_prices`, `bonuses`, `max_profit`, `current_profit`, and `combined` within each test case. After processing each test case, the final `max_profit` is printed, and the internal variables are reset for the next test case. The variable `test_cases` remains unchanged throughout the function's execution.

