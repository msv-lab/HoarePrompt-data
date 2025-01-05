#State of the program right berfore the function call: N is an integer such that 1 <= N <= 60, K is an integer such that 1 <= K <= N, and for each piece of meat, (x_i, y_i) are integers with -1000 <= x_i, y_i <= 1000, c_i is an integer such that 1 <= c_i <= 100, and the coordinates (x_i, y_i) are distinct for all pieces of meat.
def func_1(i, j):
    return math.sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
    #The program returns the Euclidean distance between the coordinates (X[i], Y[i]) and (X[j], Y[j]) of two distinct pieces of meat, calculated as the square root of the sum of the squares of the differences in their x and y coordinates.
#Overall this is what the function does:The function accepts two integer parameters `i` and `j`, and returns the Euclidean distance between the coordinates of the pieces of meat at indices `i` and `j` in the lists `X` and `Y`. The function assumes that `i` and `j` are valid indices for the lists and that the coordinates correspond to distinct pieces of meat.

