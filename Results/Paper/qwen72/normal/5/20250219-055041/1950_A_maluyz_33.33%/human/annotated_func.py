#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are digits (integers) such that 0 <= a, b, c <= 9.
def func():
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a == b == c:
            print('NONE')
        elif max(a, b, c) == b:
            print('PEAK')
        else:
            print('NONE')
        
    #State: `t` is an integer such that 1 <= t <= 1000, `i` is `t-1`, and for each test case, `a`, `b`, and `c` are input integers. If `a < b < c`, then this relationship holds. Otherwise, it is not the case that `a < b < c`. If `a`, `b`, and `c` are all equal, then they are equal to each other. If `a`, `b`, and `c` are not all equal, then the maximum of `a`, `b`, and `c` is either `a` or `c`, but not `b`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 1000`. It then processes `t` test cases, each consisting of three integers `a`, `b`, and `c` (digits between 0 and 9). For each test case, the function prints one of the following strings based on the relationship between `a`, `b`, and `c`: 'STAIR' if `a < b < c`, 'PEAK' if `b` is the maximum of the three and `a` and `c` are not equal to `b`, or 'NONE' in all other cases. After processing all test cases, the function completes without returning any value.

