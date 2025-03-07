#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, a, b, and c are integers such that 0 <= a, b, c <= 9.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000; `a`, `b`, and `c` are the integers provided by the input in the last iteration; `n` is greater than or equal to the number of iterations executed; `i` is equal to `n` after the loop has finished executing.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c`. It then prints 'STAIR' if `a` is less than `b` and `b` is less than `c`, prints 'PEAK' if `a` is less than `b` and `b` is greater than `c`, and prints 'NONE' for any other configuration of `a`, `b`, and `c`.

