#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
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
        
    #State: `t` is the integer input by the user such that 1 ≤ t ≤ 1000, and the loop has executed `t` times. For each of the `t` iterations, `a`, `b`, and `c` are the integers read from the input such that 0 ≤ a, b, c ≤ 9. The loop has printed 'STAIRS' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The variables `a`, `b`, and `c` hold the values from the last iteration, and `i` is equal to `t` after the loop finishes.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c`. It then prints 'STAIRS' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise.

