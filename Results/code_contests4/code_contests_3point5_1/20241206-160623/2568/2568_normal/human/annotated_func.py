#State of the program right berfore the function call: **Precondition**: **n is an integer such that 4 <= n <= 300. xi and yi are integers such that -1000 <= xi, yi <= 1000.**
def func_1(x1, x2, x3, y1, y2, y3):
    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    return area / 2
    #The program returns half of the calculated area based on the initial values of `x1`, `x2`, `x3`, `y1`, `y2`, and `y3`
#Overall this is what the function does:The function `func_1` accepts integer parameters `x1`, `x2`, `x3`, `y1`, `y2`, and `y3`. It calculates the area of a triangle using the provided coordinates and returns half of this calculated area. The function assumes `x1`, `x2`, `x3`, `y1`, `y2`, and `y3` are integers. It does not perform any input validation or check for degenerate cases where the points may not form a valid triangle.

