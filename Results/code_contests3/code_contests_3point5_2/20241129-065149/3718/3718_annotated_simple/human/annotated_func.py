#State of the program right berfore the function call: x1, y1, x2, y2 are integers such that |x1|, |y1|, |x2|, |y2| <= 10^4.**
def func_1(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #The program returns the Euclidean distance between the points (x1, y1) and (x2, y2) where x1, y1, x2, y2 are integers with absolute values less than or equal to 10^4.
#Overall this is what the function does:The function func_1 accepts four integer parameters x1, y1, x2, y2 with absolute values less than or equal to 10^4 and calculates the Euclidean distance between the points (x1, y1) and (x2, y2) using the distance formula.

