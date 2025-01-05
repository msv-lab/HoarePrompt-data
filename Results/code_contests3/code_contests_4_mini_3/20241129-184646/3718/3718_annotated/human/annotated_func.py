#State of the program right berfore the function call: x1, y1, x2, and y2 are integers representing the coordinates of two cities, and the values are within the range of -10,000 to 10,000.
def func_1(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #The program returns the distance between the two cities represented by coordinates (x1, y1) and (x2, y2) using the distance formula.
#Overall this is what the function does:The function accepts four integer parameters representing the coordinates of two cities: (x1, y1) and (x2, y2). It calculates and returns the Euclidean distance between these two points using the distance formula. The function does not handle any potential edge cases, such as the input values being out of the specified range (-10,000 to 10,000), but it will compute the distance accurately as long as the inputs are valid integers.

