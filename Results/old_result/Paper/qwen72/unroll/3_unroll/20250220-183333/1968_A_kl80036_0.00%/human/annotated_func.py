#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, x is an integer such that 2 <= x <= 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, y is the integer result of x // 2 where x is an integer such that 2 <= x <= 1000.
#Overall this is what the function does:The function `func` processes a series of test cases. It first reads an integer `t` (1 <= t <= 1000) indicating the number of test cases. For each test case, it reads an integer `x` (2 <= x <= 1000) and prints the integer result of `x` divided by 2 (i.e., `x // 2`). After processing all test cases, the function does not return any value, but the state of the program is such that `t` test cases have been processed, and for each test case, the result of `x // 2` has been printed.

