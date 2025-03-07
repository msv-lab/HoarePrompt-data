#State of the program right berfore the function call: No variables are passed to the function func_1. The function is designed to read input from the standard input, which is expected to be a line of space-separated integers.
def func_1():
    return map(int, input().split())
    #The program returns a map object that contains the integers obtained from the input line of space-separated integers.
#Overall this is what the function does:The function `func_1` reads a line of space-separated integers from the standard input and returns a map object that contains these integers. No variables are passed to the function, and the final state of the program includes a map object that can be iterated over to access the integers.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_2` does not take any parameters.
def func_2():
    return list(func_1())
    #The program returns a list that is the result of calling the function `func_1()`. Since `func_1()` is not defined in the initial state, the specific contents of the list cannot be determined.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a list that is the result of calling another function `func_1()`. The specific contents of the list are undefined because `func_1()` is not provided in the code.

