#State of the program right berfore the function call: None. The function does not take any parameters and is used to read input from the user, converting it into integers.
def func_1():
    return map(int, input().split())
    #The program returns a map object that contains the integers obtained from the user input, where each input value is split by spaces and converted to an integer.
#Overall this is what the function does:The function `func_1` reads a line of input from the user, splits the input by spaces, converts each split value to an integer, and returns a map object containing these integers. The function does not take any parameters and does not modify any external state. After the function concludes, the user will have a map object that can be iterated over to access the integers.

#State of the program right berfore the function call: None of the variables in the function signature are used, so there are no specific preconditions related to the function's input.
def func_2():
    return list(func_1())
    #The program returns a list that is the result of calling the function `func_1()`. The contents of the list depend on the implementation of `func_1()`, which is not provided.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a list that is the result of calling `func_1()`. The contents of the list depend on the implementation of `func_1()`.

