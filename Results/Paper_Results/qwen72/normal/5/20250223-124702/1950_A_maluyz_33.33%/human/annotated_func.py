#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are digits (integers) such that 0 <= a, b, c <= 9.
def func():
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a == b == c:
            print('NONE')
        elif max(a, b, c) == b:
            print('PEAK')
        else:
            print('NONE')
        
    #State: The loop has finished executing all iterations for the given value of t. The values of a, b, and c for each test case have been processed, and the appropriate output ('STAIR', 'PEAK', or 'NONE') has been printed for each test case. The variables a, b, and c are not retained between iterations, and their final values are undefined. The value of t remains unchanged.
#Overall this is what the function does:The function `func` processes `t` test cases, where `t` is an integer between 1 and 1000. For each test case, it reads three digits `a`, `b`, and `c` (each between 0 and 9) and prints 'STAIR' if `a < b < c`, 'PEAK' if `a <= b >= c` and `b` is the maximum, and 'NONE' otherwise. The function does not return any value, and the state of the program after the function concludes is that all test cases have been processed and the appropriate output has been printed for each. The variables `a`, `b`, and `c` are not retained between iterations, and their final values are undefined. The value of `t` remains unchanged.

