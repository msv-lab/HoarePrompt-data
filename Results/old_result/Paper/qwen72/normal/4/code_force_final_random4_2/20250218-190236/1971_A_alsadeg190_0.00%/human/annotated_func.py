#State of the program right berfore the function call: The function should be called within a loop that processes t test cases, where t is a non-negative integer such that 1 <= t <= 100. For each test case, x and y are non-negative integers such that 0 <= x, y <= 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: `x` and `y` are input integers, `i` is `x-1`. If `x` > `y`, then `x` is greater than `y`. Otherwise, `x` is less than or equal to `y`. `x` must be greater than or equal to `x` for the loop to execute all iterations.
#Overall this is what the function does:The function `func` processes a series of test cases. It first reads an integer `x` from the input, which represents the number of test cases to process. For each test case, it reads two non-negative integers `x` and `y` from the input. It then prints the two integers in ascending order. After processing all test cases, the function completes without returning any value. The final state of the program is that `x` and `y` are the last input integers, and `i` is `x-1` (where `x` is the number of test cases).

