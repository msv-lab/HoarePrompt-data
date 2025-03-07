#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, a, b, and c are integers such that 0 <= a, b, c <= 9.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000; `a`, `b`, and `c` are integers input by the user such that 0 <= a, b, c <= 9; `q` is greater than 0; `i` is equal to `q`. The loop has finished executing all `q` iterations.
#Overall this is what the function does:The function reads an integer `q` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` (each between 0 and 9 inclusive). It then prints 'STAIR' if `a` is less than `b` and `b` is less than `c`, prints 'PEAK' if `a` is less than `b` and `b` is greater than `c`, and prints 'NONE' otherwise.

