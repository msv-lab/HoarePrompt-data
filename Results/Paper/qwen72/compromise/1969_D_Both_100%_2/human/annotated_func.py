#State of the program right berfore the function call: None
def func_1():
    return int(read_input())
    #The program returns an integer value input by the user.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads an input from the user and returns it as an integer. The final state of the program after the function concludes is that it has returned an integer value provided by the user.

#State of the program right berfore the function call: None of the variables are passed to the function `func_2`. This function reads input from the standard input and splits it into a list of integers.
def func_2():
    return map(int, read_input().split())
    #The program returns a map object that converts each element from the input string, which is split by spaces, into an integer. The input string is read from the standard input.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads a line of input from the standard input, splits the input string by spaces, converts each element into an integer, and returns a map object containing these integers. The final state of the program after the function concludes is that a map object is returned, which can be iterated over to access the converted integers.

#State of the program right berfore the function call: primary_items is a list of tuples where each tuple contains two integers representing the price for Alice and the price for Bob, respectively. secondary_heap is a list of tuples where each tuple contains two integers representing the price for Alice and the price for Bob, respectively.
def func_3(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: `primary_items` is a list of tuples, `secondary_heap` is a list of tuples, and `total` is the sum of the first elements in all tuples in `secondary_heap` plus the sum of the first and second elements of all tuples in `primary_items` where the sum of the first and second elements is non-negative.
    return total
    #The program returns the sum of the first elements in all tuples in `secondary_heap` plus the sum of the first and second elements of all tuples in `primary_items` where the sum of the first and second elements is non-negative.
#Overall this is what the function does:The function `func_3` takes two parameters, `primary_items` and `secondary_heap`, both of which are lists of tuples containing two integers each. It calculates and returns the sum of the first elements in all tuples in `secondary_heap` plus the sum of the first and second elements of all tuples in `primary_items` where the sum of the first and second elements is non-negative. The original lists `primary_items` and `secondary_heap` remain unchanged.

#State of the program right berfore the function call: test_cases is a positive integer representing the number of test cases, n and k are non-negative integers such that 0 ≤ k ≤ n, prices is a list of integers representing the prices Alice pays for the items, bonuses is a list of integers representing the bonuses Bob pays for the items, and both prices and bonuses have the same length n.
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
        
    #State: After the loop executes all iterations, `test_cases` is 0, `_` is `k-1` for the last iteration, `k` is the value returned by `func_2()` for the last iteration, `heap` contains the `k` tuples with the highest second elements from the last `combined` list, `remaining_items` is an empty list, `n` and `k` are the values returned by `func_2()` for the last iteration, `prices` is a list containing the values returned by `func_2()` for the last iteration, `neg_prices` is a list where each element is the negation of the corresponding element in `prices` for the last iteration, `bonuses` is a list containing the values returned by `func_2()` for the last iteration, `combined` is an empty list, `current_profit` is the final adjusted profit after processing all items in `combined` for the last iteration, and `max_profit` is the maximum profit observed during the loop execution for the last iteration. The variables `test_cases`, `n`, `prices`, `neg_prices`, and `bonuses` remain unchanged for each iteration, but their values are updated based on the return values of `func_2()` for each new iteration.
#Overall this is what the function does:The function `func_4` processes a series of test cases, where each test case involves calculating the maximum profit Alice can achieve by selecting up to `k` items from a list of items. Each item has a price (from the `prices` list) and a bonus (from the `bonuses` list). The function reads the number of test cases and, for each test case, reads the values of `n` (the number of items) and `k` (the number of items to select), along with the `prices` and `bonuses` lists. It then calculates the maximum profit by considering the combined effect of prices and bonuses, ensuring that the selected items maximize the total profit. The function prints the maximum profit for each test case. After all test cases are processed, the function completes its execution, and the state of the program reflects the final values of the variables used in the last test case, with `test_cases` being 0.

