#State of the program right berfore the function call: radius is a non-negative float or integer, and height is a non-negative float or integer.
def func_1(radius, height):
    return 1 / 3 * math.pi * radius ** 2 * height
    #The program returns the volume of a cone calculated as (1/3) * π * radius² * height, where radius is a non-negative float or integer and height is a non-negative float or integer.
#Overall this is what the function does:The function accepts two parameters, `radius` and `height`, both of which are expected to be non-negative floats or integers. It calculates and returns the volume of a cone using the formula (1/3) * π * radius² * height. The function does not handle invalid inputs such as negative values or non-numeric types, which could lead to runtime errors.

