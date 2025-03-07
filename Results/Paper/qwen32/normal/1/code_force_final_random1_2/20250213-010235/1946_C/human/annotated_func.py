#State of the program right berfore the function call: No variables in the function signature.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: The input read from `sys.stdin.readline()` is a positive integer `n`, and the function `solve()` has been executed `n` times.
    #
    #Using the required format:
    #Output State:
#Overall this is what the function does:The function `func_1` reads a positive integer `n` from standard input and then executes the `solve()` function `n` times. It does not accept any parameters and does not return a value; its primary action is to invoke `solve()` multiple times based on the input.

