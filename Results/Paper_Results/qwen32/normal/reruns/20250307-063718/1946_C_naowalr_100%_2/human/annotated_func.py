#State of the program right berfore the function call: This function does not have any parameters. It reads input from standard input, processes multiple test cases, and does not return any value.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: The integer read from `sys.stdin.readline()` is 0, and `solve()` has been executed the number of times specified by the initial integer read from `sys.stdin.readline()`.
#Overall this is what the function does:The function reads an integer from standard input that specifies the number of test cases. It then processes each test case by calling the `solve()` function the specified number of times. The function does not accept any parameters and does not return any value.

