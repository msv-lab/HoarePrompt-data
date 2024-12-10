#State of the program right berfore the function call: base is a positive float representing the area of the triangular base, height is a positive float representing the height of the triangular prism, and length is a positive float representing the length of the prism.
def func_1(base, height, length):
    base_area = 0.5 * base * height
    volume = base_area * length
    return volume
    #The program returns the volume, which is a positive value equal to base_area multiplied by length, where base_area is equal to 0.5 * base * height.
#Overall this is what the function does:The function accepts three positive float parameters `base`, `height`, and `length`, and calculates and returns the volume of a triangular prism using the formula `0.5 * base * height * length`. The returned volume will always be a positive float since all input parameters are positive.

