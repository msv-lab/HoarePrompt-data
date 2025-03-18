#State of the program right berfore the function call: None. The function does not take any parameters and is used to read input from the user, converting it into a list of integers.
def func_1():
    return map(int, input().split())
    #The program returns a map object that converts each element from the user's input, which is split by spaces, into an integer.
#Overall this is what the function does:The function `func_1` reads a space-separated sequence of numbers from the user and returns a map object that converts each element into an integer. The function does not take any parameters and does not modify any external state. After the function concludes, the user's input is transformed into a map object of integers, which can be further processed or converted to a list or other iterable as needed.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_2` does not take any parameters.
def func_2():
    return list(func_1())
    #The program returns a list that is the result of calling the function `func_1()`. Since `func_1()` is not defined in the initial state, the exact contents of the list cannot be determined.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It returns a list that is the result of calling the function `func_1()`. The exact contents of the list cannot be determined without the definition of `func_1()`.

