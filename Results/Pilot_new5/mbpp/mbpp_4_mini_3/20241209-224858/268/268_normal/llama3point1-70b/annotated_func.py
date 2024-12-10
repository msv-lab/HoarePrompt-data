#State of the program right berfore the function call: matrix is a list of lists (2D list) of numbers, and n is a non-negative integer such that 0 <= n < len(matrix[0]) if matrix is not empty.
def func_1(matrix, n):
    return max(row[n - 1] for row in matrix)
    #The program returns the maximum value from the nth column (where n is a non-negative integer) of the 2D list 'matrix'
#Overall this is what the function does:The function accepts a 2D list `matrix` of numbers and a non-negative integer `n`, and returns the maximum value from the nth column of the matrix, assuming `n` is valid and within the range of the matrix's columns. If `n` is out of bounds, it may raise an `IndexError`.

