#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 represents the initial number of stones in each pile. It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.
def func():
    tc = int(input())
    while tc > 0:
        n = int(input())
        
        arr = sorted(list(set([int(x) for x in input().split(' ')])), reverse=True) + [
            0]
        
        dp = True
        
        n = len(arr) - 1
        
        for i in range(1, n):
            dp = arr[i] - arr[i + 1] > 1 or not dp
        
        print('Alice' if dp else 'Bob')
        
        tc -= 1
        
    #State: Output State: The output state will be a series of strings either "Alice" or "Bob", each corresponding to the result of one test case's execution within the loop.
    #
    #Explanation: For each test case (`tc`), the code reads an integer `n` and a list of integers from the user. It then sorts this list in descending order, removes duplicates, appends a zero, and initializes a boolean `dp` to `True`. A loop checks if the difference between consecutive elements is greater than 1 or if `dp` is `False`. If the condition is met for any pair of consecutive elements, `dp` remains `True`; otherwise, it becomes `False`. Finally, it prints "Alice" if `dp` is still `True`, indicating that no two consecutive elements differ by exactly 1, or "Bob" if `dp` is `False`. After processing each test case, `tc` is decremented until it reaches 0, at which point all test cases have been processed.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and a list of `n` integers representing the initial number of stones in each pile. It then sorts this list in descending order, removes duplicates, and appends a zero. The function checks if the difference between any two consecutive elements in the list is exactly 1. If such a pair is found, it sets a boolean `dp` to `False`; otherwise, `dp` remains `True`. Finally, it prints "Alice" if `dp` is `True`, indicating that no two consecutive elements differ by exactly 1, or "Bob" if `dp` is `False`. The function continues this process for all test cases until all test cases are processed.

