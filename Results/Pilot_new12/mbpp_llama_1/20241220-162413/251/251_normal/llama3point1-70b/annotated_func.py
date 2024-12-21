#State of the program right berfore the function call: x and y are real numbers.
def func_1(x, y):
    r = math.hypot(x, y)
    phi = math.atan2(y, x)
    return r, phi
    #The program returns `r`, the distance from the origin to the point (`x`, `y`), and `phi`, the angle in radians from the positive x-axis to the line segment connecting the origin to (`x`, `y`), both derived from the real numbers `x` and `y`.
#Overall this is what the function does:The function `func_1` accepts two real number parameters, `x` and `y`, and returns a tuple containing two values: `r`, the Euclidean distance from the origin to the point (`x`, `y`), and `phi`, the angle in radians from the positive x-axis to the line segment connecting the origin to (`x`, `y`). The function handles all possible real number inputs for `x` and `y`, including zero and negative values, and returns the corresponding distance and angle. The returned distance `r` is always non-negative, while the angle `phi` is in the range [-π, π]. The function does not perform any error checking or handling for non-real number inputs. After the function concludes, the input variables `x` and `y` remain unchanged, and the returned values `r` and `phi` represent the calculated distance and angle, respectively.

