#State of the program right berfore the function call: matrix is a list of lists of numbers, and n is a non-negative integer such that 0 <= n < len(matrix[0]).
def func_1(matrix, n):
    nth_column = [row[n] for row in matrix]
    return max(nth_column)
    #The program returns the maximum value from the n-th column of the list of lists 'matrix'
#Overall this is what the function does:The function accepts a list of lists of numbers `matrix` and a non-negative integer `n`, and returns the maximum value from the n-th column of `matrix`. It assumes that `n` is within the bounds of the number of columns in the matrix. If `matrix` is empty or `n` is out of bounds, the behavior is undefined as the maximum function will raise an error. Therefore, it is important to ensure that `matrix` is non-empty and that `n` is valid before calling this function.

