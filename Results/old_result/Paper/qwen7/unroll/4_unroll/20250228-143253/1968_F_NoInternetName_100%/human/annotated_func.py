#State of the program right berfore the function call: cast is a callable object that can convert strings to a numeric type (e.g., int or float), and the input is a space-separated string of integers.
def func_1(cast):
    return map(cast, input().split())
    #The program returns a map object containing the integers converted from a space-separated string using the callable object 'cast'.
#Overall this is what the function does:The function accepts a callable object `cast` that can convert strings to a numeric type, and returns a map object containing integers converted from a space-separated string using the callable object `cast`.

