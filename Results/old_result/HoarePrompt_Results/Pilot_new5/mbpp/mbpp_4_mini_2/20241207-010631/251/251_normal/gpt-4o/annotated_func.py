#State of the program right berfore the function call: x and y are floating-point numbers representing the rectangular coordinates.
def func_1(x, y):
    r = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan2(y, x)
    return r, theta
    #The program returns r, which is the square root of x, and theta, which is the angle calculated as math.atan2(y, x)
#Overall this is what the function does:The function accepts two floating-point numbers `x` and `y`, representing rectangular coordinates, and returns `r`, the distance from the origin to the point (x, y), and `theta`, the angle in radians from the positive x-axis to the point (x, y).

