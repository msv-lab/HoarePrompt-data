#State of the program right berfore the function call: N is an integer such that 1 <= N <= 60; K is an integer such that 1 <= K <= N; each piece of meat has coordinates (x_i, y_i) where -1000 <= x_i, y_i <= 1000 and (x_i, y_i) are distinct for all i; c_i is an integer such that 1 <= c_i <= 100.
def func_1(i, j):
    return math.sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
    #The program returns the Euclidean distance between the points (X[i], Y[i]) and (X[j], Y[j]) based on their coordinates, where X[i] and Y[i] are distinct integers within the range of -1000 to 1000.
#Overall this is what the function does:The function accepts two integer parameters `i` and `j`, and returns the Euclidean distance between the points defined by their coordinates (X[i], Y[i]) and (X[j], Y[j]). The coordinates X and Y are assumed to be lists of integers within the range of -1000 to 1000, and the function assumes that the indices `i` and `j` are valid and correspond to distinct points. There are no checks for index validity or handling of cases where `i` and `j` might be out of bounds.

