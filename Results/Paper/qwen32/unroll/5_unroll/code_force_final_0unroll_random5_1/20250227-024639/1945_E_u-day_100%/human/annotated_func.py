#State of the program right berfore the function call: No variables are present in the function signature. This function is expected to read input from standard input and return a map object of integers.
def func_1():
    return map(int, input().split())
    #The program returns a map object that contains integers converted from the space-separated values read from standard input.
#Overall this is what the function does:The function `func_1` reads space-separated values from standard input, converts them to integers, and returns a map object containing these integers.

#State of the program right berfore the function call: This function does not have any parameters. It relies on the output of another function `func_1()`, which is expected to return a list.
def func_2():
    return list(func_1())
    #The program returns a list that is the output of the function `func_1()`
#Overall this is what the function does:The function `func_2` returns a list that is the output of the function `func_1()`. It does not accept any parameters.

