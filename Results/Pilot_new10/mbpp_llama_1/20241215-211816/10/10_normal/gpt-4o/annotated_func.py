#State of the program right berfore the function call: base, height, and length are positive numbers.
def func_1(base, height, length):
    base_area = 0.5 * base * height
    volume = base_area * length
    return volume
    #The program returns the volume which is 0.5 times the product of a positive base, a positive height, and a positive length
#Overall this is what the function does:The function accepts three parameters `base`, `height`, and `length`, and returns their volume, calculated as 0.5 times the product of these three values, without any validation or error handling for non-positive input values.

