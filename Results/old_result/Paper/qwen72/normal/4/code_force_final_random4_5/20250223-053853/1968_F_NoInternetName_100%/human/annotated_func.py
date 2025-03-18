#State of the program right berfore the function call: cast is a callable that can be used to convert the input strings into the desired type (e.g., int, float).
def func_1(cast):
    return map(cast, input().split())
    #The program returns an iterator that applies the `cast` function to each element of the input string split by spaces.
#Overall this is what the function does:The function `func_1` accepts a callable `cast` and returns an iterator that applies the `cast` function to each element of an input string split by spaces. The input string is provided by the user through the `input()` function. After the function concludes, the returned iterator can be used to iterate over the converted elements.

