#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a and b are integers such that 1 <= a, b <= 10^9.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: The variable `t` remains unchanged, and for each test case, the program prints 'Yes' if at least one of the integers `a` or `b` is even, otherwise it prints 'No'.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `a` and `b`. For each test case, it prints 'Yes' if at least one of the integers is even, otherwise it prints 'No'.

