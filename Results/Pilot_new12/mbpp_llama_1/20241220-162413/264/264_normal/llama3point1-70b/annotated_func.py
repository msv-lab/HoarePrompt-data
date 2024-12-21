#State of the program right berfore the function call: deg is a number (either an integer or a float) representing an angle in degrees.
def func_1(deg):
    return deg * math.pi / 180
    #The program returns the angle in radians, which is the result of converting 'deg' from degrees to radians using the conversion factor math.pi / 180, where 'deg' is the input angle in degrees.
#Overall this is what the function does:The function converts an input angle in degrees to its equivalent angle in radians, accepting a single parameter `deg` which can be either an integer or a float, and returns the converted value, covering all potential cases including positive, negative, and zero degree inputs, as well as non-integer degree values, without modifying the input parameter or performing any error checking on the type or range of the input angle.

