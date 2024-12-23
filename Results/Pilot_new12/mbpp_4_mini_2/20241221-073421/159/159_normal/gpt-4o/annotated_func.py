#State of the program right berfore the function call: radius and height are non-negative numbers.
def func_1(radius, height):
    return 1 / 3 * math.pi * radius ** 2 * height
    #The program returns the volume of a cone calculated as (1/3) * π * radius² * height, where radius and height are non-negative numbers.
#Overall this is what the function does:The function accepts two non-negative numbers, `radius` and `height`, and calculates the volume of a cone using the formula (1/3) * π * radius² * height. The function returns this volume. It does not handle cases where the inputs are negative or non-numeric, which could lead to runtime errors. However, if both inputs are valid, the function accurately computes and returns the volume of the cone, ensuring that the specification aligns with the mathematical definition.

