#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are digits such that 0 <= a, b, c <= 9.
def func():
    q = int(input())
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: t remains an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are digits such that 0 <= a, b, c <= 9; q is an input integer. The loop has printed 'STAIR', 'PEAK', or 'NONE' for each iteration based on the values of a, b, and c.
#Overall this is what the function does:The function `func` reads an integer `q` from the input, representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` from the input. It then prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. After processing all `q` test cases, the function concludes without returning any value. The state of the program remains unchanged except for the side effect of printing the results.

