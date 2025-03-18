#State of the program right berfore the function call: The function should be called within a loop that processes t test cases, where t is a non-negative integer such that 1 <= t <= 100. For each test case, x and y are non-negative integers such that 0 <= x, y <= 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: `x` and `y` are input integers, `i` is `x-1`, and `x` must be greater than 0. If `x` < `y`, the values of `x`, `y`, and `i` remain unchanged. Otherwise, the values of `x`, `y`, and `i` also remain unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an integer `x` from the input, and for each value of `x`, it reads `x` pairs of non-negative integers `x` and `y` (each pair on a new line). For each pair, it prints the two integers in ascending order. The function does not return any value. After the function concludes, the input values have been processed and printed, but no changes are made to any external variables or state.

