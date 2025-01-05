#State of the program right berfore the function call: **Precondition**: **x1, y1, x2, y2 are integers such that -10^4 <= x1, y1, x2, y2 <= 10^4 and x1 != x2 or y1 != y2.**
def func_1(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #The program returns the Euclidean distance between the points (x1, y1) and (x2, y2)
#Overall this is what the function does:The function accepts four integers x1, y1, x2, y2 representing two points and calculates the Euclidean distance between them using the formula sqrt((x1 - x2)

