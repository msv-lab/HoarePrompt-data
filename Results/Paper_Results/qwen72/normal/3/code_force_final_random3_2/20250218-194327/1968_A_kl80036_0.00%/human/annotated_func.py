#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, x is an integer such that 2 <= x <= 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: `t` is an integer such that 1 <= t <= 1000, and for each of the t test cases, `x` is an integer such that 2 <= x <= 1000, `y` is `x // 2` which is the integer division of `x` by 2, and `i` is `t - 1`.
#Overall this is what the function does:The function `func` processes a series of test cases, where the number of test cases `t` is an integer between 1 and 1000, inclusive. For each test case, it reads an integer `x` from the input, where `2 <= x <= 1000`, and prints the integer division of `x` by 2. After processing all test cases, the function does not return any value, but the state of the program is such that `t` test cases have been processed, and for each test case, the result of `x // 2` has been printed.

