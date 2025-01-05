#State of the program right berfore the function call: **Input**

- N: an integer representing the total number of pieces of meat (1 <= N <= 60)
- K: an integer representing the number of pieces of meat Takahashi wants to eat (1 <= K <= N)
- (x_i, y_i, c_i): N sets of integers representing the coordinates and hardness of each piece of meat (-1000 <= x_i, y_i <= 1000, 1 <= c_i <= 100)

**Output**

- The time required to have K or more pieces of meat ready if Takahashi put the heat source to minimize this time, with an absolute or relative error at most 10^-6.
def func_1(i, j):
    return math.sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
    #The program returns the distance between pieces of meat i and j based on their coordinates X[i], Y[i], X[j], Y[j]
#Overall this is what the function does:The function func_1 accepts two indices i and j representing pieces of meat, calculates the Euclidean distance between these two pieces based on their coordinates X[i], Y[i], X[j], Y[j], and returns the result. The function ensures that the distance is calculated accurately and returns it.

