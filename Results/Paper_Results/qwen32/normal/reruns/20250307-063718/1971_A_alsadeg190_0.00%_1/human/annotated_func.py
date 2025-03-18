#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each of the t test cases, x and y are integers such that 0 <= x, y <= 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: The loop has executed `t` times, where `t` is the initial integer input indicating the number of test cases. For each of the `t` iterations, the loop reads two integers `x` and `y` (with `0 <= y <= 9`) from the input. If `x` is greater than `y`, it prints `x` followed by `y`. Otherwise, it prints `y` followed by `x`. The variables `x` and `y` are updated in each iteration based on the new input values, but `t` remains unchanged throughout the loop execution.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, where 1 <= t <= 100. For each test case, it reads two integers `x` and `y`, where 0 <= x, y <= 9, and prints the larger of the two integers followed by the smaller one.

