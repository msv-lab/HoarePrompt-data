#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each of the t test cases, x and y are integers such that 0 <= x, y <= 9.
def func():
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: Output State: `t` remains the input integer, and for each of the `t` test cases, `x` and `y` are lists containing 10 integers each, where each integer is between 0 and 9 (inclusive).
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: The value of `t` remains unchanged, and for each of the `t` test cases, the loop prints a pair of integers for each index `i` from 0 to 9. The pair is either `x[i]` and `y[i]` if `x[i]` is less than `y[i]`, or `y[i]` and `x[i]` if `x[i]` is greater than or equal to `y[i]`. The lists `x` and `y` remain unchanged.
#Overall this is what the function does:The function `func` accepts an integer `t` (1 <= t <= 100) representing the number of test cases. For each test case, it reads two integers `x` and `y` (0 <= x, y <= 9) from user input. After reading the inputs, the function prints a pair of integers for each test case, ensuring that the first integer in the pair is always less than or equal to the second integer. The function does not return any value, and the lists `x` and `y` remain unchanged after the function concludes.

