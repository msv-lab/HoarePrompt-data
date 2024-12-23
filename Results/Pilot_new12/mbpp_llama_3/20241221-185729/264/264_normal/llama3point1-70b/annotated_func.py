#State of the program right berfore the function call: deg is a real number representing an angle in degrees.
def func_1(deg):
    return deg * math.pi / 180
    #The program returns the angle in radians, which is the result of multiplying the angle in degrees by pi and then dividing by 180
#Overall this is what the function does:The function `func_1` takes an angle in degrees as input and returns the equivalent angle in radians. It accepts a single parameter `deg`, a real number, and returns the result of the conversion, which is calculated by multiplying `deg` by `math.pi` and then dividing by 180. This conversion is performed for all real number inputs, including positive, negative, and zero values, as well as non-integer values, without any explicit error handling or input validation. The function's output will be a real number representing the angle in radians, regardless of the input value. Note that the function does not modify the input value `deg` and does not have any side effects. The function will return a result for all valid input values, but it does not handle cases where the input is not a real number, such as complex numbers, strings, or other non-numeric inputs.

