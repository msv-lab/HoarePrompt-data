#State of the program right berfore the function call: x1, y1, x2, and y2 are integers representing the coordinates of two cities, and r1 and r2 are positive integers representing the respective distances from each city to the attacking enemy rings, where |x1|, |y1|, |x2|, |y2| ≤ 10^4 and 1 ≤ r1, r2 ≤ 10^4.
def func_1(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #The program returns the Euclidean distance between the two cities located at coordinates (x1, y1) and (x2, y2)
#Overall this is what the function does:The function accepts four integer parameters representing the coordinates of two cities: (x1, y1) and (x2, y2). It calculates and returns the Euclidean distance between these two cities based on their coordinates. The function does not handle any potential edge cases such as checking for invalid input types or ensuring the inputs are within the specified range; it simply computes the distance using the Euclidean formula.

