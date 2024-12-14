#State of the program right berfore the function call: matrix is a list of lists where each inner list represents a row in the matrix, and n is an integer such that 0 <= n < len(matrix[0]).
def func_1(matrix, n):
    return max(row[n - 1] for row in matrix)
    #The program returns the maximum value among the nth-1 element of each row in the matrix
#Overall this is what the function does:The function accepts a matrix (a list of lists) and an integer `n`, and returns the maximum value among the `(n-1)`th element of each row in the matrix.

