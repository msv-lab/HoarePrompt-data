#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are digits such that 0 <= a, b, c <= 9.
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
        
    #State: The loop has completed all iterations, and the values of t, a, b, and c remain unchanged. The output state depends on the input values provided for each test case during the loop execution. For each test case, if a < b < c, 'STAIRS' is printed; if a < b > c, 'PEAK' is printed; otherwise, 'NONE' is printed.
#Overall this is what the function does:The function `func` reads an integer `t` (1 <= t <= 1000) from the input, representing the number of test cases. For each test case, it reads three digits `a`, `b`, and `c` (0 <= a, b, c <= 9) from the input. Based on the values of `a`, `b`, and `c`, the function prints 'STAIRS' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' for all other cases. After processing all test cases, the function completes and the values of `t`, `a`, `b`, and `c` are no longer relevant.

