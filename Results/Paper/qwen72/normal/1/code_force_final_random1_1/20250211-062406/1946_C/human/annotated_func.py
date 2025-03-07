#State of the program right berfore the function call: None
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: The input read from `sys.stdin` must be a valid integer greater than or equal to the number of iterations specified, and the `solve()` function has been called the number of times specified by the input.
#Overall this is what the function does:The function `func_1` reads an integer from standard input (`sys.stdin`) and calls the `solve` function that many times. It does not accept any parameters and does not return any value. After the function completes, the input from `sys.stdin` will have been consumed, and the `solve` function will have been executed the specified number of times.

