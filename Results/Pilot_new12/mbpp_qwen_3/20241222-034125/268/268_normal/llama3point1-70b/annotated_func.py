#State of the program right berfore the function call: matrix is a list of lists where each inner list represents a row in the matrix, and n is an integer such that 0 <= n < the number of columns in the matrix.
def func_1(matrix, n):
    return max(row[n - 1] for row in matrix)
    #The program returns the maximum value of the element located in the position (n-1) in each row of the matrix
#Overall this is what the function does:The function `func_1` accepts a matrix (a list of lists) and an integer `n`, and returns the maximum value of the element located in the position `(n-1)` in each row of the matrix. The function iterates over each row in the matrix, accesses the element at index `n-1` in each row, and computes the maximum value among these elements. The function handles the case where `n` is within the bounds of the matrix columns, but does not handle cases where `n` is out of bounds, which would result in an `IndexError`. If the matrix is empty or `n` is outside the valid range, the function will raise an `IndexError`.

