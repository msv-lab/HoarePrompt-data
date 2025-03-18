#State of the program right berfore the function call: The function should be called within a loop that iterates t times, where t is an integer such that 1 <= t <= 1000. For each iteration, the function receives three integers a, b, and c as input, where each integer is between 0 and 9 inclusive.
def func():
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIRS')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: `t` is an integer such that 1 <= `t` <= 1000, `i` is `t-1`, and `a`, `b`, and `c` are the input integers. For each iteration from 0 to `t-1`, if `a < b < c`, then the condition `a < b < c` holds and 'STAIRS' is printed. If `a < b > c`, then the condition `a < b > c` holds and 'PEAK' is printed. Otherwise, neither `a < b < c` nor `a < b > c` holds and 'NONE' is printed.
#Overall this is what the function does:The function `func` is designed to be called within a loop that iterates `t` times, where `t` is an integer such that 1 <= `t` <= 1000. For each iteration, it reads three integers `a`, `b`, and `c` (0 <= `a`, `b`, `c` <= 9) from the input. It then prints 'STAIRS' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. After `t` iterations, the function completes, and the program state is such that `t` iterations have been processed, with the appropriate output printed for each set of inputs.

