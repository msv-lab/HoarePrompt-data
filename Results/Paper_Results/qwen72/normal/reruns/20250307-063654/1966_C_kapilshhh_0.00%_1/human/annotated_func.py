#State of the program right berfore the function call: The function should take two parameters: an integer t representing the number of test cases, and a list of lists, where each inner list contains integers representing the number of stones in each pile for a test case. Each integer in the inner lists is positive and does not exceed 10^9, and the length of each inner list is between 1 and 2 * 10^5. The sum of the lengths of all inner lists does not exceed 2 * 10^5.
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
        
    #State: The loop has executed `t` times, `tc` is 0, and for each test case, the output is 'Alice' if there exists any difference between consecutive elements in the sorted unique list `arr` (excluding the last 0) that is greater than 1; otherwise, the output is 'Bob'.
#Overall this is what the function does:The function `func` takes no parameters and reads input from the user. It processes `t` test cases, where `t` is an integer provided by the user. For each test case, it reads an integer `n` and a list of integers representing the number of stones in each pile. The function then checks if there is any difference greater than 1 between consecutive elements in the sorted unique list of stones (excluding the last 0). If such a difference exists, it prints 'Alice'; otherwise, it prints 'Alice' (which seems to be a mistake, as it always prints 'Alice'). After processing all test cases, `tc` is 0, and the function has printed 'Alice' for each test case.

