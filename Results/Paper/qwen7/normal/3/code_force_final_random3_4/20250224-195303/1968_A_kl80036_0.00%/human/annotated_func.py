#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, x is an integer such that 2 ≤ x ≤ 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: Output State: After the loop executes all the iterations, `i` will be equal to `t - 1`, `t` remains a positive integer such that \(1 \leq t \leq 1000\), `x` will be the last input integer from the user, and `y` will be `x // 2`.
    #
    #This means that the loop will run exactly `t` times, incrementing `i` from 0 to `t-1`. The variable `x` will hold the value of the last input integer provided by the user during the final iteration, and `y` will be the result of dividing `x` by 2 using integer division.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of two integers: `t` (number of iterations, 1 ≤ t ≤ 1000) and `x` (an integer, 2 ≤ x ≤ 1000). For each test case, it reads `t` values of `x`, calculates `x // 2` for the last input value of `x`, and prints the result. After processing all test cases, the function ends with `t` remaining unchanged and within the specified range, `x` holding the last input value, and `y` being the result of the last integer division operation.

