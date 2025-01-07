#State of the program right berfore the function call: x and y are floating-point numbers representing the rectangular coordinates.
def func_1(x, y):
    r = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan2(y, x)
    return r, theta
    #The program returns r and theta, where r is the radial coordinate calculated as the distance from the origin to the point (x, y), and theta is the angle in radians calculated from math.atan2(y, x).
#Overall this is what the function does:The function accepts two floating-point numbers, `x` and `y`, representing rectangular coordinates, and calculates the radial coordinate `r` as the distance from the origin to the point (x, y) using the formula √(x² + y²). It also calculates the angle `theta` in radians using `math.atan2(y, x)`, which correctly handles all quadrants and edge cases, such as when `x` is 0, avoiding division by zero errors. The function returns both `r` and `theta`.

