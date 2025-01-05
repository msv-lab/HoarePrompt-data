#State of the program right berfore the function call: x1, y1, x2, and y2 are integers representing the coordinates of two cities, and each city has an associated radius r1 and r2, which are positive integers such that 1 ≤ r1, r2 ≤ 10^4. The absolute value of the coordinates does not exceed 10^4.
def func_1(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #The program returns the Euclidean distance between the two cities represented by coordinates (x1, y1) and (x2, y2)
#Overall this is what the function does:The function accepts four integer parameters x1, y1, x2, and y2, which represent the coordinates of two cities, and it returns the Euclidean distance between these two cities. The function does not account for the associated radii of the cities (r1 and r2), meaning it strictly calculates the distance based on coordinates without any radius considerations.

