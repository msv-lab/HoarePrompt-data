#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_1` does not take any arguments.
def func_1():
    return int(read_input())
    #The program returns an integer value read from user input.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads an integer value from user input and returns this integer value. After the function concludes, the program has returned an integer value that was provided by the user.

#State of the program right berfore the function call: None of the variables are passed to the function `func_2`. This function reads input from a source (likely standard input) and splits it into a list of integers.
def func_2():
    return map(int, read_input().split())
    #The program returns a map object that converts each element from the input string, split by spaces, into an integer. The input string is read from a source, likely standard input, and is expected to contain space-separated values.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads a string of space-separated values from a source (likely standard input), splits the string into individual components, and returns a map object that converts each component into an integer.

#State of the program right berfore the function call: primary_items is a list of tuples where each tuple represents an item with two integers (a_i, b_i) such that 1 ≤ a_i, b_i ≤ 10^9. secondary_heap is a list of tuples where each tuple represents an item with two integers (a_i, b_i) such that 1 ≤ a_i, b_i ≤ 10^9.
def func_3(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: After the loop has executed all iterations, `primary_items` remains a list of tuples where each tuple contains two integers (a_i, b_i). The variable `total` is updated to be the sum of the first elements of all tuples in `secondary_heap` plus the sum of the first and second elements of all tuples in `primary_items` where the sum of the first and second elements is greater than or equal to 0.
    return total
    #The program returns the value of `total`, which is the sum of the first elements of all tuples in `secondary_heap` plus the sum of the first and second elements of all tuples in `primary_items` where the sum of the first and second elements is greater than or equal to 0.
#Overall this is what the function does:The function `func_3` takes two parameters, `primary_items` and `secondary_heap`, both of which are lists of tuples containing two integers each. It calculates the sum of the first elements of all tuples in `secondary_heap` and adds to this sum the values of the first and second elements of all tuples in `primary_items` where the sum of these elements is greater than or equal to 0. The function returns this total sum. The original lists `primary_items` and `secondary_heap` remain unchanged.

#State of the program right berfore the function call: No direct variables are passed to `func_4()`. However, it internally calls `func_1()`, `func_2()`, and `func_3()` which are expected to provide the necessary inputs and process the data accordingly.
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
        
    #State: After all iterations of the loop, `test_cases` is 0, `heap` is a list containing the last `k` elements of `combined` (if `combined` had at least `k` elements) in the order they were popped from `combined`, `remaining_items` is an empty list, `n` and `k` are assigned the values returned by `func_2()` for the last iteration, `prices` is a list containing the values returned by `func_2()` for the last iteration, `neg_prices` is a list containing the negated values of `prices` for the last iteration, `bonuses` is a list containing the values returned by `func_2()` for the last iteration, `combined` is an empty list, `current_profit` is the final value after all iterations of the loop, and `max_profit` is the maximum value of `current_profit` observed during the loop.
#Overall this is what the function does:`func_4` processes multiple test cases by calling `func_1` to determine the number of test cases. For each test case, it retrieves data using `func_2` and processes this data to calculate the maximum profit possible under certain conditions. The function uses a heap to manage and optimize the selection of items based on their prices and bonuses. After processing all test cases, the function prints the maximum profit for each test case. The function does not return any value but modifies and processes the data internally.

