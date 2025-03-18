#State of the program right berfore the function call: The function should take two integers a and b as input, where 1 <= a, b <= 10^9, representing the dimensions of the rectangle. The function should also handle multiple test cases, where the number of test cases t is an integer such that 1 <= t <= 10^4.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: `t` is 0, `_` is `t-1`, and for each iteration, `a` and `b` were integers provided by the user input. If either `a` or `b` was even, the program printed 'Yes'. If both `a` and `b` were odd, the program printed 'No'.
#Overall this is what the function does:The function `func` accepts an integer `t` (1 <= t <= 10^4) representing the number of test cases. For each test case, it reads two integers `a` and `b` (1 <= a, b <= 10^9) from user input, representing the dimensions of a rectangle. After processing all test cases, the function prints 'Yes' if either `a` or `b` is even, and 'No' if both `a` and `b` are odd. The function does not return any value.

