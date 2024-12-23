#State of the program right berfore the function call: x and y are real numbers representing the rectangular coordinates.
def func_1(x, y):
    r = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan2(y, x)
    return r, theta
    #`r` is the Euclidean distance from the origin to the point (x, y), and `theta` is the angle in radians between the positive x-axis and the line segment that joins the origin with the point (x, y)
#Overall this is what the function does:The function `func_1` accepts two parameters `x` and `y`, which represent the rectangular coordinates of a point. It calculates the Euclidean distance `r` from the origin (0,0) to the point `(x, y)` using the formula \( r = \sqrt{x^2 + y^2} \). Additionally, it computes the angle `theta` in radians between the positive x-axis and the line segment joining the origin with the point `(x, y)` using the `math.atan2(y, x)` function. The function returns these two values `r` and `theta`. This function handles all edge cases appropriately, including when `x` or `y` is zero.

