#State of the program right berfore the function call: No variables in the function signature. The function `func_1` does not take any parameters.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: `solve()` has been executed `n` times, where `n` is the integer read from `sys.stdin.readline()`.
#Overall this is what the function does:The function `func_1` reads an integer from standard input, then calls the `solve` function that many times. It does not accept any parameters and does not return a value.

