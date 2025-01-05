#State of the program right berfore the function call: x1, y1, x2, and y2 are integers representing the coordinates of two different cities, and the function assumes that the cities are surrounded by flatland rings, which are defined by their respective radii given in the problem description.
def func_1(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #The program returns the Euclidean distance between the two cities represented by coordinates (x1, y1) and (x2, y2).
#Overall this is what the function does:The function accepts four integer parameters (x1, y1, x2, y2) that represent the coordinates of two cities and returns the Euclidean distance between these two cities. The function does not handle any potential issues such as the input being non-integer values or the square root of negative numbers, but it effectively computes the distance using the formula for Euclidean distance in a two-dimensional space.

