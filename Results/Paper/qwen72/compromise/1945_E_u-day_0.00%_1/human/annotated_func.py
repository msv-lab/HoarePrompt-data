#State of the program right berfore the function call: No variables are passed to the function, and it is expected to read input from the standard input, which should be a string of integers separated by spaces.
def func_1():
    return map(int, input().split())
    #The program returns a map object that converts each string element from the input (a string of integers separated by spaces) into an integer.
#Overall this is what the function does:The function `func_1` reads a string of integers separated by spaces from the standard input and returns a map object that converts each string element into an integer. No variables are passed to the function, and it does not modify any external state. The final state of the program includes the returned map object, which can be iterated over to access the converted integers.

#State of the program right berfore the function call: None of the variables are used in the function signature, so there are no preconditions related to the function's parameters.
def func_2():
    return list(func_1())
    #The program returns a list that is the result of calling the function `func_1()`. Since `func_1()` is not defined in the initial state, the specific contents of the list cannot be determined.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It returns a list that is the result of calling another function `func_1()`. The specific contents of the list depend on the implementation of `func_1()`, which is not provided.

