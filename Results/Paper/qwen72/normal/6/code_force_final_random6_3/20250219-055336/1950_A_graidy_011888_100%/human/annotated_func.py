#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are digits (integers) such that 0 <= a, b, c <= 9.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b and b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: `t` is an integer such that 1 <= t <= 1000, `a`, `b`, and `c` are digits (integers) provided by the user input, `n` is an input integer, and `i` is `n-1`. For each iteration from 0 to `n-1`, if `a < b < c`, then `a` is less than `b`, and `b` is less than `c`, and 'STAIR' is printed. If `a < b and b > c`, then `a` is less than `b`, and `b` is greater than `c`, and 'PEAK' is printed. If none of these conditions hold, then `a`, `b`, and `c` do not satisfy `a < b < c` or `a < b and b > c`, and 'NONE' is printed.
#Overall this is what the function does:The function `func` reads an integer `n` from user input, which represents the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` from user input. It then checks the relationship between these integers and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b` and `b > c`, and 'NONE' otherwise. After processing all `n` test cases, the function concludes without returning any value. The final state of the program is that `n` test cases have been processed, and the appropriate output ('STAIR', 'PEAK', or 'NONE') has been printed for each test case.

