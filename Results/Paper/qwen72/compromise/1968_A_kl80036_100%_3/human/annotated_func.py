#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each of the t test cases, x is a positive integer such that 2 <= x <= 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: For each of the t test cases, the output is the value of x - 1, where x is a positive integer such that 2 <= x <= 1000. The value of t remains unchanged.
#Overall this is what the function does:The function `func` accepts no parameters and reads input from the user. It processes `t` test cases, where `t` is a positive integer between 1 and 1000. For each test case, it reads an integer `x` (where 2 <= x <= 1000) and prints the value of `x - 1`. The value of `t` remains unchanged after the function execution.

