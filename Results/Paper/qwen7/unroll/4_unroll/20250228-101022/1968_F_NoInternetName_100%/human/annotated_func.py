#State of the program right berfore the function call: cast is a callable that can convert string to a desired type (e.g., int, float), and it is applied to each element of the input split by spaces.
def func_1(cast):
    return map(cast, input().split())
    #The program returns a map object that applies the callable 'cast' to each element of the input string split by spaces.
#Overall this is what the function does:The function accepts a callable `cast` and returns a map object that applies `cast` to each element of the input string split by spaces. The input string is processed such that each space-separated element undergoes the transformation defined by the `cast` function, resulting in a map object containing the transformed elements.

