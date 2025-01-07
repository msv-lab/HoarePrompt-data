#State of the program right berfore the function call: x and y are floating-point numbers representing the rectangular coordinates.
def func_1(x, y):
    r = math.hypot(x, y)
    phi = math.atan2(y, x)
    return r, phi
    #The program returns r, which is the hypotenuse calculated as the square root of the sum of squares of x and y, and phi, which is the angle calculated as the arctangent of the ratio of y to x.
#Overall this is what the function does:The function accepts two floating-point numbers, `x` and `y`, representing rectangular coordinates. It calculates and returns `r`, the hypotenuse (the distance from the origin to the point (x, y)), and `phi`, the angle (in radians) from the positive x-axis to the point (x, y) using the arctangent of the ratio of `y` to `x`. The function does not handle cases where both `x` and `y` are zero, which would lead to an undefined angle.

