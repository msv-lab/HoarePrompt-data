#State of the program right berfore the function call: n is an integer such that 4 ≤ n ≤ 300, and each of the points (x1, y1), (x2, y2), (x3, y3) are integers with -1000 ≤ xi, yi ≤ 1000, where no three points are collinear and no two points are identical.
def func_1(x1, x2, x3, y1, y2, y3):
    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    return area / 2
    #The program returns half of the calculated area based on the integer values of (x1, y1), (x2, y2), and (x3, y3), where area is determined by the formula area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2).
#Overall this is what the function does:The function accepts six integer parameters representing the coordinates of three distinct points (x1, y1), (x2, y2), and (x3, y3). It calculates and returns half of the area of the triangle formed by these points using the formula area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2). The expected input conditions are that no three points are collinear and no two points are identical.

