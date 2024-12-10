#State of the program right berfore the function call: matrix is a list of lists (2D list) where each inner list has the same number of elements, and n is a non-negative integer such that 0 <= n < len(matrix[0]).
def func_1(matrix, n):
    nth_column = [row[n] for row in matrix]
    return max(nth_column)
    #The program returns the maximum value from the nth column of the matrix, where nth_column contains the nth elements from each row of the matrix.
#Overall this is what the function does:The function accepts a 2D list (matrix) and a non-negative integer n, and returns the maximum value from the nth column of the matrix. It assumes that all inner lists have the same number of elements, and that n is always a valid index based on the length of the inner lists. If the matrix is empty or if the specified column does not exist, it may lead to an index error, which is not handled in the function.

