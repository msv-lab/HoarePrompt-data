#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 10, representing the length of the strip, and s is a string of length n consisting of characters 'W' and 'B', where 'W' represents a white cell and 'B' represents a black cell, with at least one cell being black.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        first_black = s.find('B')
        
        last_black = s.rfind('B')
        
        min_paint = last_black - first_black + 1
        
        print(min_paint)
        
    #State: After the loop executes all the iterations, `_` is `t-1`, `t` remains the same as the initial input, and for each test case, `n` and `s` are the inputs provided for that specific iteration. `first_black` is the index of the first occurrence of 'B' in `s` or -1 if 'B' is not found, `last_black` is the index of the last occurrence of 'B' in `s` or -1 if 'B' is not found, and `min_paint` is `last_black - first_black + 1`. The loop has printed the value of `min_paint` for each test case.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n` consisting of 'W' and 'B'. It calculates the minimum number of cells that need to be painted to cover all black cells ('B') in the string `s` and prints this value for each test case. The function does not return any value; it only prints the results. After the function completes, `t` remains unchanged, and the values of `n` and `s` for each test case are processed and discarded.

