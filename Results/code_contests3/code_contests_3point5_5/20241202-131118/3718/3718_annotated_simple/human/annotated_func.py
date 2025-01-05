#State of the program right berfore the function call: x1, y1, x2, y2 are integers such that |x1|, |y1|, |x2|, |y2| <= 10^4.**
def func_1(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #The program returns the Euclidean distance between the points (x1, y1) and (x2, y2)
#Overall this is what the function does:The function accepts four integer parameters representing two points in a Cartesian plane, calculates the Euclidean distance between these two points using the distance formula, and returns the result. The function correctly computes the Euclidean distance between the two points (x1, y1) and (x2, y2) as described in the annotations. The function handles any integer values within the specified range (-10^4 to 10^4).

