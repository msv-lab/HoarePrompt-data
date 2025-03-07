#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, x is an integer such that 2 <= x <= 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: For each of the t test cases, y is an integer such that 1 <= y <= 999, where y is the value of x - 1 from the input. The value of t remains unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads an integer `x` and prints `x - 1`.

