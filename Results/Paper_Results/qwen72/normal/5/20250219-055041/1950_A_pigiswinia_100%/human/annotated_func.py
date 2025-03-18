#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are digits (integers) such that 0 <= a, b, c <= 9.
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
        
    #State: `t` is an input integer such that 1 <= t <= 1000, `i` is `t-1`, and for each iteration `i` from 0 to `t-1`, `a`, `b`, and `c` are input integers. If `a` is less than `b` and `b` is less than `c`, then the condition `a < b < c` holds, and 'STAIR' is printed. If `a` is less than `b` and `b` is greater than `c`, then the condition `a < b > c` holds, and 'PEAK' is printed. If neither of these conditions is met, then 'NONE' is printed.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 1000`, indicating the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` from the input, where `0 <= a, b, c <= 9`. It then evaluates the relationship between `a`, `b`, and `c` and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. After processing all test cases, the function completes without returning any value.

