#State of the program right berfore the function call: None of the variables in the function signature are relevant as `func_1` does not take any parameters.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: Output State: The loop has executed the `solve()` function a number of times equal to the integer read from the standard input. The initial state of the variables outside the loop remains unchanged.
#Overall this is what the function does:The function `func_1` reads an integer from the standard input and then calls the `solve` function that many times. The function does not accept any parameters and does not return any value. After the function concludes, the `solve` function has been executed a number of times equal to the integer read from the standard input, and the state of any variables outside the function remains unchanged.

