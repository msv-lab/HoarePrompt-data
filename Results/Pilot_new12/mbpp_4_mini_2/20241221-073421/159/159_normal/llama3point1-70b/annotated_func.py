#State of the program right berfore the function call: radius is a non-negative float or integer representing the radius of the cone's base, and height is a non-negative float or integer representing the height of the cone.
def func_1(radius, height):
    return 1.0 / 3 * math.pi * radius * radius * height
    #The program returns the volume of the cone calculated using the formula (1/3) * π * radius² * height, where radius is a non-negative float or integer and height is a non-negative float or integer.
#Overall this is what the function does:The function accepts two parameters, `radius` and `height`, both of which must be non-negative floats or integers. It calculates and returns the volume of a cone using the formula (1/3) * π * radius² * height. The function does not handle cases where the input values are negative or non-numeric, so any such inputs would cause an error. The function assumes valid input as described, which is stated in the annotations. After execution, the program provides the computed volume of the cone.

