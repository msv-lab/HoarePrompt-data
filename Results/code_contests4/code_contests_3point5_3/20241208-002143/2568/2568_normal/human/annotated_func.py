#State of the program right berfore the function call: n is an integer such that 4 <= n <= 300. Each of the next n lines contain two integers xi, yi such that -1000 <= xi, yi <= 1000. No three points are on the same line and no two points coincide.**
def func_1(x1, x2, x3, y1, y2, y3):
    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    return area / 2
    #The program returns half of the area of the triangle calculated using the provided points
#Overall this is what the function does:The function `func_1` accepts 6 parameters: x1, x2, x3, y1, y2, y3, which represent the coordinates of 3 points in a triangle. It calculates the area of the triangle formed by these points using a specific formula and returns half of that area. The code assumes that the points are not collinear and do not coincide with each other.

