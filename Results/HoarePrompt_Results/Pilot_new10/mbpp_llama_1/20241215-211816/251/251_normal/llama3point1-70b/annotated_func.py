#State of the program right berfore the function call: x and y are real numbers.
def func_1(x, y):
    r = math.hypot(x, y)
    phi = math.atan2(y, x)
    return r, phi
    #The program returns `r`, which is the square root of the sum of the squares of `x` and `y`, and `phi`, which is the arctangent of `y` divided by `x` in radians.
#Overall this is what the function does:The function accepts two real numbers `x` and `y`, calculates and returns the polar coordinates (`r`, `phi`) of the point (`x`, `y`), where `r` is the Euclidean distance from the origin and `phi` is the angle from the positive x-axis in radians, handling edge cases where `x` or `y` may be zero, infinity, or NaN.

