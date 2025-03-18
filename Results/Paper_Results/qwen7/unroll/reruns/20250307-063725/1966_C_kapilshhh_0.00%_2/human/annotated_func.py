#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 represents the initial number of stones in each pile. It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The output state will be a series of strings either "Alice" or "Bob" printed based on the conditions inside the loop.
    #
    #Explanation: The loop processes `tc` test cases. For each test case, it reads an integer `n`, then a list of integers, sorts the unique elements in descending order, appends a zero, and checks a condition using dynamic programming (DP) to determine if "Alice" or "Bob" should be printed. After processing all `tc` test cases, the output will consist of "Alice" or "Bob" printed for each test case, depending on whether the condition `dp` was met or not.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of an integer `n` representing the number of piles and a list of `n` integers representing the number of stones in each pile. For each test case, it sorts the unique stones in descending order, appends a zero, and uses a condition to determine if "Alice" or "Bob" should be printed. The function prints "Alice" or "Bob" for each test case based on the outcome of the condition.

