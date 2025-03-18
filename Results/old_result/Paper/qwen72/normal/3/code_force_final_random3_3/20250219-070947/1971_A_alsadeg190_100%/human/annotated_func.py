#State of the program right berfore the function call: The function is designed to handle multiple test cases. Each test case consists of two integers x and y, where 0 <= x, y <= 9. The number of test cases t is a positive integer such that 1 <= t <= 100.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: `x` and `y` are input integers, `i` is `x-1`, and `x` must be greater than or equal to `x-1`. If `x` < `y`, no changes are made to `x`, `y`, or `i`. Otherwise, no changes are made to `x`, `y`, or `i`.
#Overall this is what the function does:The function `func` reads an integer `x` from the user, which represents the number of test cases. For each test case, it reads two integers `x` and `y` (0 <= x, y <= 9) from the user. It then prints the two integers in ascending order. After processing all test cases, the function completes without returning any value.

