#State of the program right berfore the function call: degrees is a numeric value representing an angle in degrees.
def func_1(degrees):
    return degrees * (math.pi / 180)
    #The program returns the radian equivalent of the angle 'degrees', calculated by multiplying degrees by (math.pi / 180)
#Overall this is what the function does:The function accepts a numeric value `degrees` representing an angle in degrees and returns its radian equivalent by multiplying `degrees` by (math.pi / 180). This conversion is valid for any numeric value, including negative angles and non-integer values, as the function will not check or validate the input type.

