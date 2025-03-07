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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `a`, `b`, and `c` are the integers provided by the input, `n` is the input integer, and `i` is `n-1`. For each iteration from 0 to `n-1`, if `a < b < c`, then `a` is less than `b`, and `b` is less than `c`. If `a < b and b > c`, then the condition `a < b and b > c` holds. If neither `a < b < c` nor `a < b and b > c` holds, then neither of these conditions is true.
#Overall this is what the function does:The function `func` reads an integer `n` from the input, representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` from the input. It then evaluates the relationship between these three integers and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b` and `b > c`, and 'NONE' otherwise. After processing all test cases, the function completes without returning any value.

