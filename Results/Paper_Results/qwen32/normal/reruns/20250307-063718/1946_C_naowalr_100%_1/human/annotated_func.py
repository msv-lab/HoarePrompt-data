#State of the program right berfore the function call: No variables are present in the function signature of `func_1()`. This function appears to be a wrapper that reads the number of test cases and iterates through them, calling the `solve()` function for each test case.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: The loop has executed `int(sys.stdin.readline())` times, and the `solve()` function has been called that many times.
#Overall this is what the function does:The function `func_1` reads the number of test cases from the standard input, iterates through each test case, and calls the `solve()` function for each one. It does not accept any parameters and does not return any value.

