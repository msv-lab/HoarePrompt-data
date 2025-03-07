#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_1():
    return int(read_input())
    #The program returns an integer value that is input by the user.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an integer value that is input by the user.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters. The function reads input and splits it into integers, which are then returned as a map object.
def func_2():
    return map(int, read_input().split())
    #The program returns a map object containing integer values from the input string, where the input string is split by spaces.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an input string, splits it into substrings by spaces, converts each substring into an integer, and returns a map object containing these integer values.

#State of the program right berfore the function call: primary_items is a list of tuples where each tuple contains two integers (a_i, b_i) representing the price of an item for Alice and Bob respectively, and secondary_heap is a list of tuples where each tuple contains a single integer (b_i - a_i) representing the profit Alice makes from selling the item to Bob.
def func_3(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: `primary_items` remains unchanged, `secondary_heap` remains unchanged, `total` is the initial value of `total` plus the sum of `a_i + b_i` for all tuples in `primary_items` where `a_i + b_i >= 0`.
    return total
    #The program returns the value of `total` which is the initial value of `total` plus the sum of `a_i + b_i` for all tuples in `primary_items` where `a_i + b_i` is greater than or equal to 0.
#Overall this is what the function does:The function `func_3` accepts two parameters: `primary_items`, a list of tuples (a_i, b_i), and `secondary_heap`, a list of tuples (b_i - a_i). It calculates the sum of the first elements of all tuples in `secondary_heap` and adds to this sum the values of `a_i + b_i` for all tuples in `primary_items` where `a_i + b_i` is greater than or equal to 0. The function returns the final value of this sum. The `primary_items` and `secondary_heap` lists remain unchanged after the function execution.

#State of the program right berfore the function call: No variables are directly passed to the function `func_4`. However, it relies on the outputs of `func_1` and `func_2` to provide the necessary inputs. `func_1` is expected to return the number of test cases, and `func_2` is expected to return a tuple of two integers (n, k) and lists of integers representing the item prices and bonuses.
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
        
    #State: The loop will execute `test_cases` times, and after each iteration, the variables `heap`, `remaining_items`, `n`, `k`, `prices`, `neg_prices`, `bonuses`, `max_profit`, `current_profit`, and `combined` will be reset to their initial states within the loop. The final output state will be the same as the initial state, except that `max_profit` will be printed for each test case.
#Overall this is what the function does:The function `func_4` processes a series of test cases, each defined by the number of items `n`, the number of items to select `k`, a list of item prices, and a list of item bonuses. For each test case, it calculates the maximum profit that can be achieved by selecting `k` items, considering both their prices and bonuses. The function prints the maximum profit for each test case. After processing all test cases, the function concludes, and no variables are retained or returned.

