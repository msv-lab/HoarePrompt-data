#State of the program right berfore the function call: x1, y1, x2, and y2 are integers representing the coordinates of two different cities, and both cities have a flatland ring surrounding them with a radius (r) that is a positive integer (1 ≤ r ≤ 10^4). The absolute values of x1, y1, x2, and y2 do not exceed 10^4.
def func_1(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #The program returns the Euclidean distance between the two cities located at coordinates (x1, y1) and (x2, y2)
#Overall this is what the function does:The function accepts four integer parameters (x1, y1, x2, y2) representing the coordinates of two cities and returns the Euclidean distance between them. The function does not handle any edge cases related to the input values, such as invalid or non-integer inputs, but it is designed to calculate the distance correctly for any valid integer coordinates within the specified range.

