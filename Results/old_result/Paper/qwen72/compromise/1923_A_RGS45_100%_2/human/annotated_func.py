#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 1000) representing the number of test cases, and a list of lists, where each inner list represents a test case with the first element being an integer n (2 ≤ n ≤ 50) and the second element being a list of n integers (0 ≤ a_i ≤ 1) representing the cells of the ribbon. Each test case must contain at least one chip (a_i = 1).
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: The function will print the number of zeros between the first and last occurrence of 1 for each test case, and the variables `t`, `n`, `arr`, `x`, `y`, and `z` will be updated for each iteration of the loop. After all iterations, `t` will be 0, and the values of `n`, `arr`, `x`, `y`, and `z` will be the final values from the last test case.
#Overall this is what the function does:The function `func` reads input from the user to process a series of test cases. It accepts an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string of `n` characters (each character is either '0' or '1'). The function finds the first and last occurrence of '1' in the string and prints the number of '0's between these two occurrences. If a test case does not contain a '1', the function will print 0. After processing all test cases, the function does not return any value, but it prints the results for each test case. The variables `t`, `n`, `arr`, `x`, `y`, and `z` are updated and used during the execution of the function.

