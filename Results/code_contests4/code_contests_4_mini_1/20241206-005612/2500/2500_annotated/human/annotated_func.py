#State of the program right berfore the function call: N is an integer such that 1 <= N <= 60, K is an integer such that 1 <= K <= N, and for each piece of meat i (where 1 <= i <= N), (x_i, y_i) are integers with -1000 <= x_i, y_i <= 1000, c_i is an integer such that 1 <= c_i <= 100, and (x_i, y_i) are unique pairs for different pieces of meat.
def func_1(i, j):
    return math.sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
    #The program returns the Euclidean distance between the coordinates (x_i, y_i) and (x_j, y_j) of two pieces of meat, where (x_i, y_i) and (x_j, y_j) are unique pairs for indices i and j.
#Overall this is what the function does:The function accepts two integer parameters, `i` and `j`, and returns the Euclidean distance between the coordinates of two pieces of meat located at indices `i` and `j`. The function assumes that the coordinates are stored in two separate lists `X` and `Y`, and it does not handle cases where the indices `i` or `j` are out of the bounds of these lists.

