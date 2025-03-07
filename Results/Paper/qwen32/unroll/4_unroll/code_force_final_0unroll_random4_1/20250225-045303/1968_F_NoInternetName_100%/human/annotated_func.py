#State of the program right berfore the function call: cast is a callable function that converts a string to another type, such as int or float.
def func_1(cast):
    return map(cast, input().split())
    #The program returns a map object that applies the callable function `cast` to each element of the input string, which has been split into a list of substrings.
#Overall this is what the function does:The function `func_1` takes a callable function `cast` as an argument and returns a map object. This map object applies the `cast` function to each element of an input string that has been split into a list of substrings.

