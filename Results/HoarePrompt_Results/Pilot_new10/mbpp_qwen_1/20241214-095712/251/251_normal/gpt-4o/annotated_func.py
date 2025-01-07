#State of the program right berfore the function call: x and y are real numbers representing the rectangular coordinates.
def func_1(x, y):
    r = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan2(y, x)
    return r, theta
    #The program returns the Euclidean distance \( r = \sqrt{x^2 + y^2} \) and the angle in radians \( \theta \) between the positive x-axis and the point (x, y)
#Overall this is what the function does:The function accepts two real numbers `x` and `y`, and returns the Euclidean distance \( r = \sqrt{x^2 + y^2} \) and the angle in radians \( \theta \) between the positive x-axis and the point (x, y).

