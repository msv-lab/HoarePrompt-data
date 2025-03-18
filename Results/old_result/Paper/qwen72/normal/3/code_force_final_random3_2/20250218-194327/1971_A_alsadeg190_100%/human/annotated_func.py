#State of the program right berfore the function call: The function should be called with a list of test cases, where each test case is a tuple of two integers (x, y) such that 0 <= x, y <= 9. The number of test cases, t, should be a non-negative integer where 1 <= t <= 100.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: The loop has executed `x` times, where `x` is the initial value provided in the test case. For each iteration, `x` and `y` are updated to new input integers. If the new `x` is less than the new `y`, then `x` and `y` are printed in that order. Otherwise, `y` and `x` are printed in that order. The value of `i` is `x-1` after the final iteration.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads an integer `x` from the user input, which represents the number of test cases. For each test case, it reads two integers `x` and `y` from the user input, and prints them in ascending order. The function performs this action for each of the `x` test cases. After the function concludes, the input values have been processed and printed, but no data is returned or stored.

