#State of the program right berfore the function call: radius and height are non-negative real numbers.
def func_1(radius, height):
    return 1.0 / 3 * math.pi * radius * radius * height
    #The program returns the volume of a cone, calculated as (1/3) * π * radius² * height, where both radius and height are non-negative real numbers.
#Overall this is what the function does:The function accepts two non-negative real numbers, `radius` and `height`, and returns the volume of a cone calculated as (1/3) * π * radius² * height. It does not handle negative values for `radius` or `height`, which would lead to incorrect calculations or unexpected results. Additionally, if either `radius` or `height` is zero, the volume will be zero, but the function still returns a valid numerical result.

