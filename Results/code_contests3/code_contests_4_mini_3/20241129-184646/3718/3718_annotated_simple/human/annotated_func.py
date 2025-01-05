#State of the program right berfore the function call: x1, y1, x2, and y2 are integers representing the coordinates of two cities, and the cities are guaranteed to be at different points.
def func_1(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #The program returns the Euclidean distance between the two cities located at coordinates (x1, y1) and (x2, y2)
#Overall this is what the function does:The function accepts four integer parameters representing the coordinates of two distinct cities (x1, y1) and (x2, y2), and it returns the Euclidean distance between these two points. There are no checks for the validity of the input coordinates, but it is assumed that the coordinates represent two different cities as per the input precondition.

