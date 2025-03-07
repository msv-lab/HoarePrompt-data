#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, a and b are integers such that 1 <= a, b <= 10^9.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: For each of the `t` test cases, the program will output 'Yes' if either `a` or `b` (or both) is even, and 'No' if both `a` and `b` are odd. The value of `t` and the specific values of `a` and `b` for each test case will remain unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It then outputs 'Yes' if either `a` or `b` (or both) is even, and 'No' if both `a` and `b` are odd. The values of `t`, `a`, and `b` remain unchanged after the function executes.

