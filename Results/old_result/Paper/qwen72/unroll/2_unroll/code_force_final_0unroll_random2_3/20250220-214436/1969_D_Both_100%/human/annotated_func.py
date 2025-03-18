#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_1():
    return int(read_input())
    #The program returns an integer value input by the user.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an integer value input by the user. After the function concludes, the program state includes a returned integer that represents the user's input.

#State of the program right berfore the function call: None of the variables are used in the function signature. The function reads input from the standard input and returns a map object of integers.
def func_2():
    return map(int, read_input().split())
    #The program returns a map object that contains integers converted from the input string, where the input string is split by spaces.
#Overall this is what the function does:The function `func_2` reads a space-separated string from the standard input, converts each part of the string into an integer, and returns a map object containing these integers. The function does not modify any external variables and does not have any side effects. After the function concludes, the user will have a map object that can be iterated over to access the integers.

#State of the program right berfore the function call: primary_items is a list of tuples where each tuple contains two integers representing the price of an item for Alice and Bob respectively, and secondary_heap is a list of tuples where each tuple contains one integer representing the price of an item for Bob.
def func_3(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: `total` is the sum of the prices in `secondary_heap` for Bob plus the sum of the prices in `primary_items` for both Alice and Bob where the sum of the prices for each item is non-negative.
    return total
    #The program returns the sum of the prices in `secondary_heap` for Bob plus the sum of the prices in `primary_items` for both Alice and Bob, where the sum of the prices for each item is non-negative.
#Overall this is what the function does:The function `func_3` accepts two parameters: `primary_items`, a list of tuples where each tuple contains two integers representing the prices of an item for Alice and Bob respectively, and `secondary_heap`, a list of tuples where each tuple contains one integer representing the price of an item for Bob. The function returns the total sum of prices for Bob from `secondary_heap` and the sum of prices for both Alice and Bob from `primary_items`, but only includes items where the sum of the prices for each item is non-negative.

#State of the program right berfore the function call: No variables are directly passed to `func_4()`. However, the function relies on the outputs from `func_1()`, `func_2()`, and `func_3()`. `func_1()` returns the number of test cases `test_cases` as a non-negative integer. `func_2()` is called twice in each test case: the first call returns two integers `n` and `k` where `1 <= n <= 2 * 10^5` and `0 <= k <= n`, and the second call returns lists of integers `prices` and `bonuses` each of length `n` with values in the range `1 <= price, bonus <= 10^9`.
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
        
    #State: The loop will have executed `test_cases` times, and for each iteration, the maximum profit (`max_profit`) will be printed. After all iterations, `test_cases` will be 0, and the variables `heap`, `remaining_items`, `n`, `k`, `prices`, `neg_prices`, `bonuses`, `max_profit`, `current_profit`, and `combined` will be reset to their initial states at the start of each iteration.
#Overall this is what the function does:The function `func_4` processes a series of test cases. For each test case, it receives two integers `n` and `k`, and two lists `prices` and `bonuses` of length `n`. It calculates the maximum profit that can be achieved by selecting up to `k` items, where the profit of each item is determined by its price and bonus. The function prints the maximum profit for each test case. After processing all test cases, the function has no return value, and the internal variables are reset for each test case.

