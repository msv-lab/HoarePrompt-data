#State of the program right berfore the function call: n is an integer such that 4 ≤ n ≤ 300, and each of the coordinates (x1, y1), (x2, y2), (x3, y3) are integers within the range of -1000 to 1000, with the guarantee that no three points are collinear and no two points are coincident.
def func_1(x1, x2, x3, y1, y2, y3):
    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    return area / 2
    #The program returns the area divided by 2, where area is calculated using the formula x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2
#Overall this is what the function does:The function accepts six integer parameters (x1, x2, x3, y1, y2, y3) representing the coordinates of three points in a 2D space. It calculates and returns the signed area of the triangle formed by those points, divided by 2. The function assumes the points are valid as per the provided constraints, specifically that no three points are collinear and no two points are coincident.

