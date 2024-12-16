#State of the program right berfore the function call: matrix is a list of lists (2D list) of numbers, and n is a non-negative integer such that 0 <= n < len(matrix[0]) if matrix is not empty.
def func_1(matrix, n):
    nth_column = [row[n] for row in matrix]
    return max(nth_column)
    #The program returns the maximum value from the nth column of the matrix, where nth_column contains the nth elements from each row of the matrix.
#Overall this is what the function does:The function accepts a 2D list (matrix) of numbers and a non-negative integer n, and it returns the maximum value from the nth column of the matrix. An edge case to consider is when the matrix is empty; in such a case, accessing the nth column would lead to an IndexError since there are no columns to retrieve. Therefore, adequate error handling should be implemented for an empty matrix scenario.

