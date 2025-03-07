#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, x is an integer such that 2 <= x <= 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: `t` is an integer such that 1 <= t <= 1000, `i` is `t - 1`, `x` is an integer such that 2 <= x <= 1000 for each of the t test cases, `y` is `x - 1` which is an integer such that 1 <= y <= 999 for each of the t test cases.
#Overall this is what the function does:The function `func` reads an integer `t` from user input, where `1 <= t <= 1000`, representing the number of test cases. For each test case, it reads an integer `x` from user input, where `2 <= x <= 1000`. It then calculates `y` as `x - 1` and prints the value of `y` for each test case. The function does not return any values. After the function concludes, `t` test cases have been processed, and for each test case, the value of `x - 1` has been printed.

