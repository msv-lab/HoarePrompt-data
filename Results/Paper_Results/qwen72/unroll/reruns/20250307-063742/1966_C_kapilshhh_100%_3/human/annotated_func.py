#State of the program right berfore the function call: The function should take two parameters: an integer t representing the number of test cases, and a list of lists nums where each sublist represents the piles in a test case and contains n integers (1 ≤ n ≤ 2·10^5) with each integer a_i (1 ≤ a_i ≤ 10^9) representing the initial number of stones in the i-th pile. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: The loop has finished executing all iterations, and the `tc` variable is now 0. The `dp` variable will be `True` or `False` depending on the last test case's conditions. The `n` variable will be the length of the last `arr` list minus 1. The `arr` list will be the sorted unique elements of the last input list, with an additional 0 appended at the end.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` representing the number of piles, followed by a list of integers representing the number of stones in each pile. It processes each test case by sorting the unique elements of the pile list in descending order and appending a 0 to it. The function then determines if the difference between consecutive elements in the sorted list is greater than 1, and based on this, it prints 'Alice' or 'Bob' for each test case. After processing all test cases, the function concludes with the `tc` variable set to 0, and the `dp` variable holding the result of the last test case.

