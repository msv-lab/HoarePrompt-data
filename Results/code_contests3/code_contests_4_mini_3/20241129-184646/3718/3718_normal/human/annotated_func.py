#State of the program right berfore the function call: x1, y1, x2, and y2 are integers representing the coordinates of two cities, with the additional information that each city has a corresponding detection radius r1 and r2 which are positive integers (1 ≤ r1, r2 ≤ 10^4) and the absolute values of x1, y1, x2, and y2 are less than or equal to 10^4.
def func_1(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #The program returns the Euclidean distance between the two cities represented by coordinates (x1, y1) and (x2, y2)
#Overall this is what the function does:The function accepts four integer parameters (x1, y1, x2, y2) representing the coordinates of two cities and returns the Euclidean distance between these two points. There are no checks for the detection radius or any edge cases regarding the input values, so it simply calculates the distance based solely on the provided coordinates.

