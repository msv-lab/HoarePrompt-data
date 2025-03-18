#State of the program right berfore the function call: The function should be called with a list of test cases, where each test case is a tuple of three digits (a, b, c) such that 0 <= a, b, c <= 9. The number of test cases t is a positive integer where 1 <= t <= 1000.
def func():
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: The loop will print 'STAIR', 'PEAK', or 'NONE' for each test case based on the conditions specified. The variables `a`, `b`, and `c` will be updated with the values from each test case during each iteration, but their final values will be the values from the last test case. The variable `t` will remain unchanged.
#Overall this is what the function does:The function reads an integer `t` from the input, representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` from the input. Based on the values of `a`, `b`, and `c`, it prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The function does not return any value; it only prints the results for each test case. After the function concludes, the variable `t` remains unchanged, and `a`, `b`, and `c` will hold the values from the last test case.

