#State of the program right berfore the function call: None of the variables in the function signature are used.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: The function `solve()` has been called the number of times specified by the input value read from `sys.stdin.readline()`. The initial state remains unchanged.
#Overall this is what the function does:The function `func_1` reads an integer from the standard input and calls the `solve` function that many times. The function does not accept any parameters and does not return any value. After the function concludes, the `solve` function has been executed the number of times specified by the input integer, and the initial state of the program remains unchanged.

