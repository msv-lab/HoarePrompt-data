#State of the program right berfore the function call: The function should be called with a list of test cases, where each test case is a tuple of three digits (a, b, c) such that 0 <= a, b, c <= 9, and the number of test cases t is an integer such that 1 <= t <= 1000.
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
        
    #State: The output state after the loop executes all the iterations is that the loop has printed 'STAIR', 'PEAK', or 'NONE' for each test case (a, b, c) based on the conditions provided. The variables `a`, `b`, and `c` will have their final values set to the last input values read in the last iteration of the loop, and the loop counter `i` will have the value `t-1`. All other variables that were part of the initial state but not modified within the loop will remain unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, where `1 <= t <= 1000`. For each test case, it reads three integers `a`, `b`, and `c` (with `0 <= a, b, c <= 9`). It then prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The function does not return any value. After the function concludes, the variables `a`, `b`, and `c` will hold the values from the last test case, and the loop counter `i` will be `t-1`. All other variables that were part of the initial state but not modified within the function will remain unchanged.

