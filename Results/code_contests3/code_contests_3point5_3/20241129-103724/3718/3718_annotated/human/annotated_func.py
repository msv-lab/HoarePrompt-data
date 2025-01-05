#State of the program right berfore the function call: x1, y1, x2, y2 are integers such that |x1|, |y1|, |x2|, |y2| ≤ 104.**
def func_1(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #The program returns the Euclidean distance between the points (x1, y1) and (x2, y2)
#Overall this is what the function does:The function accepts four integer parameters x1, y1, x2, y2 representing two points in a plane and calculates the Euclidean distance between these two points using the distance formula. The function then returns the calculated distance.

