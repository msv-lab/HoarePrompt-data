#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are integers such that 0 <= a, b, c <= 9.
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
        
    #State: The variables `a`, `b`, and `c` will hold the values from the last test case processed by the loop. The variable `t` will remain unchanged. The output will be a series of printed strings ('STAIR', 'PEAK', or 'NONE') corresponding to each test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` (each between 0 and 9 inclusive) and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise.

