#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: Output State: `t` is an integer such that \(1 \leq t \leq 100\), `i` is 99 (since the loop runs from `i` in `range(x)` and `x` is an input integer which can be up to 100), `x` is the first input integer, `y` is the second input integer.
    #
    #Explanation: The loop iterates `x` times, where `x` is the first input integer provided. After 99 iterations (assuming the maximum value of `x` which is 100), the final values of `i` will be 99. The values of `x` and `y` remain unchanged throughout the loop as the loop body does not modify these variables.
#Overall this is what the function does:The function processes a series of test cases defined by an integer `t`. For each test case, it reads two integers `x` and `y`, then prints them in ascending order. After processing all test cases, the function does not return any value.

