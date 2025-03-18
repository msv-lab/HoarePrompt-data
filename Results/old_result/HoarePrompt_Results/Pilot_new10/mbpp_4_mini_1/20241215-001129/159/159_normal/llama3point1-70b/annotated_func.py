#State of the program right berfore the function call: radius and height are non-negative integers or floating-point numbers.
def func_1(radius, height):
    return 1.0 / 3 * math.pi * radius * radius * height
    #The program returns the volume of a cone calculated as (1/3) * π * radius² * height, where radius and height are non-negative integers or floating-point numbers.
#Overall this is what the function does:The function accepts two parameters, `radius` and `height`, which are non-negative integers or floating-point numbers. It returns the volume of a cone calculated as (1/3) * π * radius² * height. The function does not handle invalid input cases where `radius` or `height` could be negative or non-numeric, which may lead to incorrect results or exceptions.

