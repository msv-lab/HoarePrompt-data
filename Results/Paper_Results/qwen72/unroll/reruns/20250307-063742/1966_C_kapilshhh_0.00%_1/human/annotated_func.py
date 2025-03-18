#State of the program right berfore the function call: The function should accept two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists, where each inner list contains n integers (1 ≤ n ≤ 2·10^5) representing the number of stones in each pile for a test case. Each integer a_i in the inner lists satisfies 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: `tc` is 0, `t` is an integer (1 ≤ t ≤ 10^4), and the list of lists representing the number of stones in each pile for each test case remains unchanged.
#Overall this is what the function does:The function `func` accepts an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of integers representing the number of stones in each pile. The function processes each test case to determine if a certain condition is met (related to the distribution of stones in the piles) and prints 'Alice' for each test case. After processing all test cases, the function terminates with `tc` being 0, and the original input lists remain unchanged.

