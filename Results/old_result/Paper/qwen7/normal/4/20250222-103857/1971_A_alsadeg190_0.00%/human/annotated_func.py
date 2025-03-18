#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: Output State: `t` is an integer such that \(1 \leq t \leq 100\), `i` is 99 (since the loop runs from `range(x)`, and `x` is an input integer which can be at most 100, so the maximum value of `i` would be 99), `x` is an input integer, `y` is an input integer. After all iterations of the loop, `t` remains unchanged within its initial bounds, `i` will be set to 99 (the maximum possible value since the loop runs `x` times and `x` can be at most 100), and `x` and `y` will retain their last input values from the loop's final iteration.
#Overall this is what the function does:The function processes an integer `t` where 1 ≤ t ≤ 100, representing the number of test cases. For each test case, it reads two integers `x` and `y` where 0 ≤ x, y ≤ 9. Depending on whether `x` is greater than `y`, it prints either `(x, y)` or `(y, x)`. After processing all test cases, it does not return any value but prints the results of each test case.

