#State of the program right berfore the function call: No variables are present in the function signature of `func_1`. Therefore, no precondition can be derived from the variables in the function signature.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: `solve()` has been called `int(sys.stdin.readline())` times.
#Overall this is what the function does:The function `func_1` reads an integer from standard input, which represents the number of times to execute another function named `solve()`. After executing `solve()` the specified number of times, `func_1` completes its execution without returning any value.

