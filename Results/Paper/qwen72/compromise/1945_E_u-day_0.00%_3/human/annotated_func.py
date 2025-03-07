#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_1():
    return map(int, input().split())
    #The program returns a map object that converts each element of the input string, split by spaces, into an integer.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns a map object that converts each element of an input string, split by spaces, into an integer. The input string is taken from the user via the `input()` function. After the function call, the program state includes a map object that can be iterated over to access the converted integers.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_2` does not take any parameters.
def func_2():
    return list(func_1())
    #The program returns a list that is the result of calling the function `func_1()`. Since no information is provided about the function `func_1` or its return value, the exact content of the list cannot be determined.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a list that is the result of calling the function `func_1()`. The exact content of the list cannot be determined without information about `func_1()`.

