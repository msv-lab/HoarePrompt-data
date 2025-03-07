#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_1():
    return map(int, input().split())
    #The program returns a map object that converts each element of the input string, split by spaces, into an integer.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads a line of input from the user, splits the input string by spaces, and returns a map object that converts each split element into an integer. The final state of the program after the function concludes is that it has a map object containing integers derived from the input string.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_2` does not take any parameters.
def func_2():
    return list(func_1())
    #The program returns a list that is the result of calling the function `func_1`. Since `func_1` is not defined in the initial state, we do not know the specific values or content of the list that will be returned.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a list that is the result of calling the function `func_1`. The specific values or content of the list are unknown as `func_1` is not defined in the provided code.

