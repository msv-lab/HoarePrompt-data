#State of the program right berfore the function call: x1, y1, x2, and y2 are integers representing the coordinates of two cities, where |x1|, |y1|, |x2|, |y2| ≤ 10^4.
def func_1(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #The program returns the Euclidean distance between the coordinates (x1, y1) and (x2, y2)
#Overall this is what the function does:The function accepts four integer parameters x1, y1, x2, and y2, representing the coordinates of two cities. It calculates and returns the Euclidean distance between these two points in a 2D space. The function does not handle any potential errors related to the input values or their types, but it effectively computes the distance as long as the inputs are valid integers.

