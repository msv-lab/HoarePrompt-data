#State of the program right berfore the function call: x1, y1, x2, y2 are integers such that -10^4 <= x1, y1, x2, y2 <= 10^4 and x1 != x2 or y1 != y2.**
def func_1(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #The program returns the Euclidean distance between the points (x1, y1) and (x2, y2)
#Overall this is what the function does:The function accepts four integer parameters x1, y1, x2, y2 representing two points in a 2D plane and returns the Euclidean distance between these two points. The function properly calculates the Euclidean distance formula as the square root of the sum of the squared differences of the coordinates. There are no missing functionalities or edge cases mentioned in the annotations.

