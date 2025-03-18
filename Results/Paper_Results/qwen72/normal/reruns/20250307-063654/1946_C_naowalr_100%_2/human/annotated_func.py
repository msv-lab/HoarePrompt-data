#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_1` does not take any parameters.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: `int(sys.stdin.readline())` must be greater than 0, `solve()` has been called and returned for the number of times specified by `int(sys.stdin.readline())`.
#Overall this is what the function does:The function `func_1` reads an integer from standard input and calls the `solve` function that many times. The function does not accept any parameters and does not return any value. After the function concludes, the `solve` function has been called the number of times specified by the integer read from standard input, and this integer must be greater than 0.

