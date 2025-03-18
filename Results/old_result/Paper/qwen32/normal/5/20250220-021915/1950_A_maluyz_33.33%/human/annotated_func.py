#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, a, b, and c are integers such that 0 <= a, b, c <= 9.
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
        
    #State: `t` is an integer such that 1 <= `t` <= 1000, `i` is `t-1`, and `a`, `b`, and `c` are integers provided by the input for the last iteration. The loop has finished executing all `t` iterations, and for each set of `a`, `b`, and `c` provided, the appropriate output ('STAIR', 'PEAK', or 'NONE') has been printed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, where each test case consists of three integers `a`, `b`, and `c` each ranging from 0 to 9. For each test case, the function prints 'STAIR' if `a < b < c`, 'PEAK' if `b` is the maximum of the three integers, and 'NONE' otherwise.

