#State of the program right berfore the function call: base is a positive float representing the area of the triangular base, height is a positive float representing the height of the triangular base, and length is a positive float representing the length of the prism.
def func_1(base, height, length):
    base_area = 0.5 * base * height
    volume = base_area * length
    return volume
    #The program returns the volume which is equal to 0.5 * base * height * length, where base and height are positive floats and length is a positive float
#Overall this is what the function does:The function calculates and returns the volume of a triangular prism, given the base area, height, and length as positive float parameters. Specifically, it computes the volume using the formula volume = 0.5 * base * height * length. After execution, the function guarantees that the result will be a positive float representing the volume of the prism, provided that the input values for base, height, and length are positive floats. The function does not handle cases where the inputs might be zero or negative, which could lead to incorrect results or exceptions.

