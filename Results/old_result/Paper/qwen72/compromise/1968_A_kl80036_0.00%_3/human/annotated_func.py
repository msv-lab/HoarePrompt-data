#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, x is an integer such that 2 <= x <= 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: t is an integer such that 1 <= t <= 1000, and for each test case, x is an integer such that 2 <= x <= 1000, and y is the integer result of x // 2.
#Overall this is what the function does:The function reads an integer `t` from the input, where `1 <= t <= 1000`, representing the number of test cases. For each test case, it reads an integer `x` from the input, where `2 <= x <= 1000`. It then computes `y` as the integer division of `x` by 2 and prints `y`. After processing all test cases, the function has no return value, and the state of the program includes the printed results of the integer divisions for each test case.

