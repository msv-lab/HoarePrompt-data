#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a is a list of n integers such that 1 ≤ a_i ≤ 10^9, and b is a list of n integers such that 1 ≤ b_i ≤ 10^9.
def func_1():
    return int(read_input())
    #The program returns an integer `t` such that 1 ≤ t ≤ 10^4.
#Overall this is what the function does:The function reads an integer `t` from an external source such that 1 ≤ t ≤ 10^4 and returns it. This integer `t` represents the number of test cases to process, and the function does not modify any other variables like `n`, `k`, `a`, or `b`.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a is a list of n integers such that 1 ≤ a_i ≤ 10^9, and b is a list of n integers such that 1 ≤ b_i ≤ 10^9.
def func_2():
    return map(int, read_input().split())
    #The program returns a map object containing integers extracted from the input string split by spaces.
#Overall this is what the function does:The function processes an input string, splits it into individual elements based on spaces, converts these elements to integers, and returns a map object containing these integers.

#State of the program right berfore the function call: primary_items is a list of tuples, where each tuple contains two integers (a_i, b_i); secondary_heap is a list of integers representing a min-heap of differences (b_i - a_i).
def func_3(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: Output State: `primary_items` is a list of tuples, where each tuple contains two integers (a_i, b_i); `secondary_heap` is a list of integers representing a min-heap of differences (b_i - a_i); `total` is the sum of the first elements of the tuples in `primary_items` for which the condition `item[0] + item[1] >= 0` is true.
    return total
    #The program returns the sum of the first elements of the tuples in `primary_items` for which the condition `item[0] + item[1] >= 0` is true.
#Overall this is what the function does:The function accepts a list of tuples `primary_items` and a list of integers `secondary_heap`. It calculates and returns the sum of the first elements of the tuples in `primary_items` for which the condition `item[0] + item[1] >= 0` is true.

#State of the program right berfore the function call: test_cases is a positive integer representing the number of test cases. For each test case, n and k are positive integers such that 1 ≤ n ≤ 2 \cdot 10^5 and 0 ≤ k ≤ n. prices is a list of n positive integers representing the prices for Alice (a_i), and bonuses is a list of n positive integers representing the prices for Bob (b_i).
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
        
    #State: The maximum profit obtained from executing the loop for each test case.
#Overall this is what the function does:The function processes multiple test cases, each involving a set of prices and bonuses for Alice and Bob. For each test case, it calculates the maximum possible profit by strategically combining negative prices (from Alice) and bonuses (from Bob). It uses a heap to manage the items and updates the maximum profit found during the process. After processing all test cases, it prints the maximum profit obtained from any single test case.

