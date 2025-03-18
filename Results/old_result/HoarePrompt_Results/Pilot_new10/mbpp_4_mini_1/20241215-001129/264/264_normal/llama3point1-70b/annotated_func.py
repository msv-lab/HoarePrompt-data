#State of the program right berfore the function call: deg is a floating-point number representing an angle in degrees.
def func_1(deg):
    return deg * math.pi / 180
    #The program returns the value of 'deg' converted to radians by multiplying it with math.pi/180
#Overall this is what the function does:The function accepts a floating-point number `deg` representing an angle in degrees and returns its equivalent value in radians by multiplying it with `math.pi/180`. The function does not handle negative values or any angle input that may result in an overflow, but it converts any valid floating-point number without raising errors.

