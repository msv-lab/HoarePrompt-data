#State of the program right berfore the function call: base, height, and length are non-negative numbers representing the base, height of the triangle, and length of the prism, respectively.
def func_1(base, height, length):
    base_area = 0.5 * base * height
    volume = base_area * length
    return volume
    #The program returns volume which is equal to base_area * length, where base_area is 0.5 * base * height
#Overall this is what the function does:The function accepts three non-negative parameters: `base`, `height`, and `length`. It calculates the area of the triangular base using the formula \(0.5 \times \text{base} \times \text{height}\) and then multiplies this area by the `length` to find the volume of a triangular prism. The function returns the calculated volume.

