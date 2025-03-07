#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are integers such that 0 <= a, b, c <= 9.
def func():
    q = int(input())
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: `t` is an integer such that 1 <= t <= 1000, `a`, `b`, and `c` are integers read from the input, `q` is greater than 0, and `i` is equal to `q`. The loop has finished executing all `q` iterations, and for each iteration, the values of `a`, `b`, and `c` were read from the input and the appropriate condition (`STAIR`, `PEAK`, or `NONE`) was printed based on the comparison of `a`, `b`, and `c`.
#Overall this is what the function does:The function reads an integer `q` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` (each ranging from 0 to 9) and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise.

