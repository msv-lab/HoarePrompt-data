#State of the program right berfore the function call: The function should be called with a list of test cases, where each test case is a tuple containing an integer n (2 ≤ n ≤ 50) and a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ 1), representing the state of the ribbon. Each test case must have at least one cell containing a chip (a_i = 1).
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: The function will print the number of zeros between the first and last occurrence of 1 in each test case for `t` iterations. The variables `n`, `arr`, `x`, `y`, and `z` will be updated for each iteration based on the input provided, but their values will not persist between iterations. After all iterations are complete, the variables `n`, `arr`, `x`, `y`, and `z` will hold the values from the last iteration, and the function will have printed the results for each test case.
#Overall this is what the function does:The function `func` reads a series of test cases from the standard input. Each test case consists of an integer `n` (2 ≤ n ≤ 50) followed by a list of `n` integers (0 or 1) representing the state of a ribbon. The function prints the number of zeros between the first and last occurrence of 1 in each test case. The function does not return any value, and the variables used within the function do not persist between test cases. After processing all test cases, the function will have printed the results for each one, and the variables will hold the values from the last test case.

