#State of the program right berfore the function call: x and y are real numbers representing the rectangular coordinates.
def func_1(x, y):
    r = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan2(y, x)
    return r, theta
    #The program returns r which is \(\sqrt{x^2 + y^2}\) and theta which is the angle in radians between the positive x-axis and the point (x, y)
#Overall this is what the function does:The function `func_1` accepts two real numbers `x` and `y`, representing the rectangular coordinates of a point. It calculates the distance `r` from the origin to the point (x, y) using the formula \( r = \sqrt{x^2 + y^2} \) and the angle `theta` in radians between the positive x-axis and the point (x, y) using the `math.atan2(y, x)` function. The function then returns these two values, `r` and `theta`. 

Potential edge cases and missing functionality:
1. If both `x` and `y` are zero, `math.sqrt(x

