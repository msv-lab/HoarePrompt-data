#State of the program right berfore the function call: x1, y1, x2, and y2 are integers representing the coordinates of two distinct cities, and r1 and r2 are integers representing the radii of the flatland rings surrounding each city, where |x1|, |y1|, |x2|, |y2| ≤ 10^4 and 1 ≤ r1, r2 ≤ 10^4.
def func_1(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #The program returns the Euclidean distance between the two distinct cities represented by coordinates (x1, y1) and (x2, y2)
#Overall this is what the function does:The function accepts four integer parameters x1, y1, x2, and y2, which represent the coordinates of two distinct cities. It calculates and returns the Euclidean distance between these two cities. The function assumes the coordinates are within the specified bounds, but does not handle cases where the inputs are not distinct or invalid, as it directly computes the distance without any checks.

