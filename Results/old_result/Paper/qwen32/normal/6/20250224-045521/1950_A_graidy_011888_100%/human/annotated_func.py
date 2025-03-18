#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
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
        
    #State: After `n` iterations, the loop has finished executing. The values of `a`, `b`, and `c` are the last set of integers read from the input, and `i` is equal to `n`. The variable `t` remains unchanged as it was in the initial state, and `n` remains the same as well.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c`. It then prints "STAIR" if `a` is less than `b` and `b` is less than `c`, prints "PEAK" if `a` is less than `b` and `b` is greater than `c`, and prints "NONE" for all other cases.

