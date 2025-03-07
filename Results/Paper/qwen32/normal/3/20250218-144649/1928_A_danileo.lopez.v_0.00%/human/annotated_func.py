#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, a and b are integers such that 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `a` and `b` are integers read from the input for each of the `t` test cases. For each test case, if either `a` or `b` (or both) is even, the program prints 'Yes'. Otherwise, if both `a` and `b` are odd, the program prints 'No'. After all `t` iterations, the loop terminates and no further input is processed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each of the `t` test cases, it reads two integers `a` and `b`. It then prints 'Yes' if either `a` or `b` (or both) is even, and 'No' if both `a` and `b` are odd.

