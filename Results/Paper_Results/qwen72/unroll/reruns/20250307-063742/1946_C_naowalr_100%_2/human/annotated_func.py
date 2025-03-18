#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_1` does not take any parameters.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: Output State: The loop has executed the `solve()` function a number of times equal to the integer value read from the standard input. The initial state of the variables remains unchanged as the loop does not modify any variables outside its scope.
#Overall this is what the function does:The function `func_1` reads an integer from the standard input and then calls the `solve` function that many times. It does not accept any parameters and does not return any value. The function does not modify any variables outside its scope, and its primary purpose is to repeatedly execute the `solve` function based on user input.

