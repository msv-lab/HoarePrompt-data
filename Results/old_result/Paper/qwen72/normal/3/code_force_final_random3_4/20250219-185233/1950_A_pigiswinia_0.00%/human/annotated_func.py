#State of the program right berfore the function call: The function should be called in a loop where the loop runs t times, with t being a non-negative integer such that 1 <= t <= 1000. For each iteration, the function should receive three digits a, b, c as input, where each digit is an integer such that 0 <= a, b, c <= 9.
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
        
    #State: `t` is a non-negative integer provided by the user such that 1 <= `t` <= 1000, `i` is `t-1`, and for each iteration from 0 to `t-1`, `a`, `b`, and `c` are integers provided by the user. For each set of `a`, `b`, and `c` provided, if `a` < `b` < `c`, the output is 'STAIRS'. If `a` < `b` > `c`, the output is 'PEAK'. Otherwise, the output is 'NONE'.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, where `1 <= t <= 1000`. It then runs a loop `t` times, and in each iteration, it reads three integers `a`, `b`, and `c` from the user, where `0 <= a, b, c <= 9`. For each set of `a`, `b`, and `c`, the function prints 'STAIRS' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The function does not return any value. After `t` iterations, the function completes and the program returns to the state it was in before the function was called.

