#State of the program right berfore the function call: The function should take two parameters: an integer t representing the number of test cases, and a list of lists, where each sublist contains integers a_1, a_2, ..., a_n representing the number of stones in each pile for a test case. t should satisfy 1 ≤ t ≤ 10^4, and for each test case, the number of piles n should satisfy 1 ≤ n ≤ 2·10^5, and the number of stones in each pile a_i should satisfy 1 ≤ a_i ≤ 10^9. The sum of n over all test cases should not exceed 2·10^5.
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
        
    #State: `tc` is 0, `t` remains unchanged, and the list of lists remains unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from input, representing the number of test cases. For each test case, it reads an integer `n` and a list of integers `arr` from input, processes the list to determine if a certain condition is met, and prints 'Alice' for each test case. After processing all test cases, `tc` is 0, and the function does not return any value. The input `t` and the list of lists remain unchanged.

