#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a is a list of n integers such that 1 ≤ a_i ≤ 10^9, and b is a list of n integers such that 1 ≤ b_i ≤ 10^9.
def func_1():
    return int(read_input())
    #The program returns an integer t, where 1 ≤ t ≤ 10^4.
#Overall this is what the function does:The function processes multiple test cases defined by an integer \( t \) (where \( 1 \leq t \leq 10^4 \)). For each test case, it reads integers \( n \) and \( k \) (where \( 1 \leq n \leq 2 \cdot 10^5 \) and \( 0 \leq k \leq n \)), and two lists \( a \) and \( b \) (where \( 1 \leq a_i \leq 10^9 \) and \( 1 \leq b_i \leq 10^9 \)). After processing these inputs, the function returns an integer \( t \) (where \( 1 \leq t \leq 10^4 \)).

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a and b are lists of integers such that for each i, 1 ≤ a_i ≤ 10^9 and 1 ≤ b_i ≤ 10^9.
def func_2():
    return map(int, read_input().split())
    #The program returns a map object containing integers split from the input string.
#Overall this is what the function does:The function processes an input string and returns a map object containing integers split from the input string.

#State of the program right berfore the function call: primary_items is a list of tuples, where each tuple contains two integers (a_i, b_i); secondary_heap is a list of integers representing a min-heap of differences (b_i - a_i) for each item.
def func_3(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: Output State: `primary_items` is a list of tuples, where each tuple contains two integers (a_i, b_i); `secondary_heap` is a list of integers representing a min-heap of differences (b_i - a_i) for each item; `total` is the sum of the first elements (a_i) of all items in `primary_items` where the sum of the tuple elements (a_i + b_i) is greater than or equal to 0.
    return total
    #The program returns the sum of the first elements (a_i) of all items in `primary_items` where the sum of the tuple elements (a_i + b_i) is greater than or equal to 0.
#Overall this is what the function does:The function accepts a list of tuples `primary_items`, where each tuple contains two integers (a_i, b_i), and a list of integers `secondary_heap` representing a min-heap of differences (b_i - a_i) for each item. It calculates and returns the sum of the first elements (a_i) of all items in `primary_items` where the sum of the tuple elements (a_i + b_i) is greater than or equal to 0.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n and k are positive integers such that 1 ≤ n ≤ 2 \cdot 10^5 and 0 ≤ k ≤ n. prices is a list of n integers where 1 ≤ price_i ≤ 10^9, and bonuses is a list of n integers where 1 ≤ bonus_i ≤ 10^9.
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
        
    #State: The maximum profit achievable across all test cases based on the given logic within the loop.
#Overall this is what the function does:The function processes multiple test cases, each defined by positive integers \( n \) and \( k \), and two lists of integers, `prices` and `bonuses`. For each test case, it calculates the maximum profit achievable by combining elements from both lists under specific conditions. It then prints the maximum profit for each test case. The function does not return any value but prints the results for each test case.

