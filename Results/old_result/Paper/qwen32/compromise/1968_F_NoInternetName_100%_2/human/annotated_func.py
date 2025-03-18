#State of the program right berfore the function call: cast is a callable function that can convert strings to a specific type, such as int or float.
def func_1(cast):
    return map(cast, input().split())
    #The program returns a map object that applies the `cast` function to each element of the input string split by spaces.
#Overall this is what the function does:The function accepts a callable `cast` function and returns a map object that applies this `cast` function to each element of an input string split by spaces.

