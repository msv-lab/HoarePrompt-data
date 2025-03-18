#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the list of integers a_1, a_2, ..., a_n represents the initial number of stones in each of the n piles, where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The output state will consist of multiple lines, each containing either "Alice" or "Bob". The number of lines will be equal to the value of `tc` provided initially. Each line corresponds to the result of one iteration of the loop based on the input values provided during that iteration.
    #
    #For each iteration, the program processes the input as follows:
    #1. It reads an integer `n`.
    #2. It takes a list of integers as input, sorts it in descending order, removes duplicates, and appends a zero.
    #3. It initializes a boolean variable `dp` to `True`.
    #4. It iterates through the list to check if the difference between consecutive elements (or the last element and zero) is greater than 1 or if `dp` remains `False`.
    #5. Based on the final value of `dp`, it prints "Alice" or "Bob".
    #6. It decrements `tc` by 1.
    #
    #The exact output will depend on the specific inputs provided during each iteration, but the process described above will be repeated until `tc` becomes 0.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and a list of `n` integers representing the number of stones in each pile. It then sorts the list in descending order, removes duplicates, and appends a zero. The function checks if the difference between consecutive elements (or the last element and zero) is greater than 1 or if a boolean variable `dp` remains `False`. Based on this check, it prints "Alice" or "Bob". This process is repeated for each test case until all test cases are processed.

