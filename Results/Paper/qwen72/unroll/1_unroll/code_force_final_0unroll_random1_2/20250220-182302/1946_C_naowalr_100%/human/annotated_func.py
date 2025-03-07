#State of the program right berfore the function call: No variables are passed to the function `func_1`.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: The loop has executed the `solve()` function a number of times equal to the integer input read from `sys.stdin`. No variables are passed to or modified within the loop, so no other variables are affected.
#Overall this is what the function does:The function `func_1` reads an integer from standard input and then calls the `solve` function that many times. It does not accept any parameters and does not return any value. The state of the program after the function concludes is that the `solve` function has been executed a number of times equal to the integer input read from `sys.stdin`. No other variables are affected by the execution of `func_1`.

