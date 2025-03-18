#State of the program right berfore the function call: No variables in the function signature. The function `func_1` does not take any parameters and its purpose is to read input and call the `solve` function for each test case.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: The integer read from `sys.stdin.readline()` iterations of `solve()` have been executed, and the number of remaining iterations is 0.
#Overall this is what the function does:The function `func_1` reads an integer from standard input, which represents the number of test cases, and then calls the `solve` function for each of those test cases.

