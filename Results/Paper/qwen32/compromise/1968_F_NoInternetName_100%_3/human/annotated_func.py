#State of the program right berfore the function call: cast is a function that can convert strings to another type, input() provides a string of space-separated values which can be successfully converted by the cast function.
def func_1(cast):
    return map(cast, input().split())
    #The program returns a map object that applies the `cast` function to each element in the list of space-separated values provided by `input()`.
#Overall this is what the function does:The function `func_1` takes a conversion function `cast` as a parameter, reads a string of space-separated values from the input, applies the `cast` function to each value, and returns a map object containing the converted values.

