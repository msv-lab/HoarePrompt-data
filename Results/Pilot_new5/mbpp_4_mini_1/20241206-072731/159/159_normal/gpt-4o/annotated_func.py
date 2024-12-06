#State of the program right berfore the function call: radius is a non-negative float or integer, and height is a non-negative float or integer.
def func_1(radius, height):
    return 1 / 3 * math.pi * radius ** 2 * height
    #The program returns the volume of a cone calculated as 1/3 * π * radius^2 * height, where radius is a non-negative float or integer and height is a non-negative float or integer.
#Overall this is what the function does:The function accepts non-negative float or integer parameters `radius` and `height`, and calculates the volume of a cone using the formula \( \frac{1}{3} \pi \times \text{radius}^2 \times \text{height} \). It does not handle negative or invalid input cases, and will return a valid volume as long as both inputs are non-negative.

