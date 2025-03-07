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
        
    #State: The loop has executed `t` times, where `t` is an input integer such that 1 <= t <= 1000. For each of the `t` iterations, the integers `a`, `b`, and `c` are provided by the input. Depending on the values of `a`, `b`, and `c` in each iteration, the program prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The variables `a`, `b`, `c`, and `i` are updated in each iteration, but `t` remains unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` (each between 0 and 9). It then prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise.

