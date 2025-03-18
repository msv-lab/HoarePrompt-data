#State of the program right berfore the function call: cast is a function that can cast or convert the input values, typically to an integer or another type.
def func_1(cast):
    return map(cast, input().split())
    #The program returns an iterator that applies the `cast` function to each element of the input string split by spaces. The input string is provided by the user at runtime.
#Overall this is what the function does:The function `func_1` accepts a parameter `cast`, which is a function for casting or converting values. It returns an iterator that applies the `cast` function to each element of an input string split by spaces. The input string is provided by the user at runtime.

