#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_1` does not take any parameters.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: Output State: None of the variables in the function signature are used, as the function `func_1` does not take any parameters. The loop iterates a number of times specified by the input, and each iteration calls the `solve()` function. The state of any other variables not affected by the loop head and body remains unchanged.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads an integer from the standard input, and for each iteration up to the number specified by this integer, it calls the `solve()` function. The function does not return any value. The state of any other variables not affected by the loop or the `solve()` function calls remains unchanged.

