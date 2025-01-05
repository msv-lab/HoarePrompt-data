#State of the program right berfore the function call: x1, y1, x2, and y2 are integers representing the coordinates of two different cities, and the radius of the flatland rings surrounding these cities must be positive integers (1 ≤ ri ≤ 10^4) with the absolute value of the coordinates not exceeding 10^4.
def func_1(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #The program returns the distance between the two cities represented by their coordinates (x1, y1) and (x2, y2), calculated using the formula sqrt((x1 - x2)
#Overall this is what the function does:The function accepts four integer parameters `x1`, `y1`, `x2`, and `y2`, which represent the coordinates of two different cities. It calculates and returns the Euclidean distance between these cities using the formula `sqrt((x1 - x2)

