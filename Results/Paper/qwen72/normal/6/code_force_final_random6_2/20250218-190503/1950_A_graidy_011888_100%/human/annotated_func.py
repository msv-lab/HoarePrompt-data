#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are integers such that 0 <= a, b, c <= 9.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `a`, `b`, and `c` are integers provided by the user input, `n` must be greater than or equal to the number of iterations, and `i` is `n - 1`. For each iteration, if `a < b < c`, the condition `a < b < c` is true and 'STAIR' is printed. If `a < b` and `b > c`, the condition `a < b and b > c` is true and 'PEAK' is printed. Otherwise, neither `a < b < c` nor `a < b and b > c` is true and 'NONE' is printed.
#Overall this is what the function does:The function `func` reads an integer `n` from the user input, which represents the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` from the user input. It then checks the relationship between these integers and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b` and `b > c`, and 'NONE' otherwise. The function does not return any value but affects the program state by reading input and printing output based on the conditions.

