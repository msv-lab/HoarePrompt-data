#State of the program right berfore the function call: base is a positive float or integer representing the area of the triangular base, height is a positive float or integer representing the height of the triangular prism, and length is a positive float or integer representing the length of the prism.
def func_1(base, height, length):
    base_area = 0.5 * base * height
    volume = base_area * length
    return volume
    #The program returns the volume of the triangular prism, which is equal to 0.5 * base * height * length
#Overall this is what the function does:The function accepts three parameters: base, height, and length, all of which should be positive floats or integers. It calculates and returns the volume of the triangular prism using the formula 0.5 * base * height * length. There are no checks for negative or zero values for the parameters, which could lead to incorrect computations or intuitions if called with invalid inputs.

