#State of the program right berfore the function call: No variables are present in the function signature of `func_1()`.
def func_1():
    return map(int, input().split())
    #The program returns a map object that contains integers derived from the input string, where the input string is split by spaces.
#Overall this is what the function does:The function `func_1` takes no input parameters, reads a line of input from the user, splits it into substrings based on spaces, converts each substring into an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: This function does not have any parameters in its signature, so there are no variables to describe. It seems to be a placeholder or a function that relies on other functions to perform its task.
def func_2():
    return list(func_1())
    #The program returns a list that is the result of calling `func_1()`
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a list that is the result of calling `func_1()`.

