#State of the program right berfore the function call: n is an integer such that 4 <= n <= 300. Each of the next n lines contains two integers xi, yi such that -1000 <= xi, yi <= 1000 and no three points are on the same line.**
def func_1(x1, x2, x3, y1, y2, y3):
    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    return area / 2
    #The program returns half of the calculated area of the triangle
#Overall this is what the function does:The function `func_1` accepts 6 integer parameters representing the coordinates of 3 points forming a triangle. It calculates the area of the triangle using the given coordinates and returns half of that calculated area. The function correctly implements the calculation of the triangle's area based on the provided coordinates.

