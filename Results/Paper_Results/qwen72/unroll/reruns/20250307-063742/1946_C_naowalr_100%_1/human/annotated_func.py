#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_1` does not take any parameters.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: Output State: The loop has executed the `solve()` function a number of times equal to the integer value read from the standard input. The initial state of the variables is unchanged because no variables are used in the function signature or modified within the loop body. The only change is that the `solve()` function has been called multiple times, but the state of the variables outside the loop remains the same as the initial state.
#Overall this is what the function does:The function `func_1` reads an integer from the standard input and calls the `solve` function that many times. The function does not accept any parameters and does not return any value. The state of the program remains unchanged except for the side effects of the `solve` function calls.

