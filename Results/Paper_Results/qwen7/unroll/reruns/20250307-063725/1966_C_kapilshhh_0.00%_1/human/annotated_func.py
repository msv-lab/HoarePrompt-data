#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 represents the initial number of stones in each pile. The sum of n over all test cases does not exceed 2⋅10^5.
def func():
    tc = int(input())
    while tc > 0:
        n = int(input())
        
        arr = sorted(list(set([int(x) for x in input().split(' ')])), reverse=True) + [
            0]
        
        dp = True
        
        n = len(arr) - 1
        
        for i in range(1, len(arr)):
            dp = arr[i] - (arr[i + 1] if i < n else 0) > 1 or not dp
        
        print('Alice' if dp else 'Alice')
        
        tc -= 1
        
    #State: Output State: The output state will be a series of strings either "Alice" or "Bob" based on the conditions inside the loop for each iteration of `tc`.
    #
    #Explanation: For each value of `tc`, the loop processes an input integer `n` and a list of integers. It then sorts this list in descending order, adds a zero at the end, and checks a condition using dynamic programming (`dp`). If the condition is met, it prints "Alice"; otherwise, it prints "Bob". This process repeats until `tc` becomes 0. Therefore, the final output state will consist of "Alice" or "Bob" printed for each iteration of `tc`.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it accepts an integer `n` (1 ≤ n ≤ 2⋅10^5) and a list of `n` integers representing the initial number of stones in each pile. It sorts this list in descending order, adds a zero at the end, and checks a specific condition using dynamic programming. If the condition is met, it prints "Alice"; otherwise, it prints "Bob". This process repeats for each test case. The function does not return any value but prints "Alice" or "Bob" for each test case.

