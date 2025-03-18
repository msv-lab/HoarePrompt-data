#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, a, b, and c are integers such that 0 <= a, b, c <= 9.
def func():
    q = int(input())
    mn = 100
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        
        if a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: `t` is an integer such that 1 <= t <= 1000, `a`, `b`, and `c` are integers provided by the input, `q` is greater than or equal to `i`, `mn` is 100, `i` is equal to `q`. The loop has finished executing all `q` iterations.
#Overall this is what the function does:The function reads an integer `q` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c`. It then prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise.

