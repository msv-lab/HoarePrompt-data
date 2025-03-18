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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `a`, `b`, and `c` are integers read from the input, `n` is greater than 0, and `i` has reached the value of `n`. The loop has executed `n` times, with each iteration reading new values of `a`, `b`, and `c` from the input and printing 'STAIR', 'PEAK', or 'NONE' based on the conditions specified.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise.

