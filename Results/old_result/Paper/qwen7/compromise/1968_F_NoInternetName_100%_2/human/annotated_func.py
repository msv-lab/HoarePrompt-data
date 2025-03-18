#State of the program right berfore the function call: cast is a callable function that can convert strings to the appropriate type (e.g., int), and the input is a space-separated string of integers or other types that can be converted using cast.
def func_1(cast):
    return map(cast, input().split())
    #The program returns a map object that applies the callable function 'cast' to each element in the input string after splitting it by spaces. The input string should contain space-separated values that can be converted to the appropriate type using the 'cast' function.
#Overall this is what the function does:The function accepts a callable function `cast` and returns a map object that applies `cast` to each element in the input string after splitting it by spaces. The input string should consist of space-separated values that can be converted to the appropriate type using the `cast` function.

