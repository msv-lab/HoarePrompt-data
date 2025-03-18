#State of the program right berfore the function call: base is a positive float representing the area of the triangular base, height is a positive float representing the height of the triangular prism, and length is a positive float representing the length of the prism.
def func_1(base, height, length):
    base_area = 0.5 * base * height
    volume = base_area * length
    return volume
    #The program returns the volume of the triangular prism, which is equal to 0.5 * base * height * length
#Overall this is what the function does:The function accepts three positive float parameters: `base`, `height`, and `length`, and returns the volume of a triangular prism calculated as 0.5 * base * height * length. There are no checks for negative or zero values, so if any of the inputs are non-positive, the behavior may not be defined.

