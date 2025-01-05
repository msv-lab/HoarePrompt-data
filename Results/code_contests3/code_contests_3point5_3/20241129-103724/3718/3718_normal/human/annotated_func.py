#State of the program right berfore the function call: x1, y1, x2, y2 are integers such that |x1|, |y1|, |x2|, |y2| ≤ 104.**
def func_1(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #The program returns the square root of the sum of the squared differences between x1 and x2, and y1 and y2. The variables x1, y1, x2, y2 are integers such that |x1|, |y1|, |x2|, |y2| ≤ 104.
#Overall this is what the function does:The function `func_1` accepts four integer parameters x1, y1, x2, and y2, and calculates the Euclidean distance between the points (x1, y1) and (x2, y2) by finding the square root of the sum of squared differences. The function correctly handles cases where x1, y1, x2, y2 are integers within the range -104 to 104.

