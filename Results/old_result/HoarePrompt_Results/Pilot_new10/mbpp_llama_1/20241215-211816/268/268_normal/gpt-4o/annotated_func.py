#State of the program right berfore the function call: matrix is a 2D list of elements, and n is a non-negative integer such that 0 <= n < len(matrix[0]).
def func_1(matrix, n):
    nth_column = [row[n] for row in matrix]
    return max(nth_column)
    #The program returns the maximum value from the list of elements at index `n` in each row of `matrix`, which are the elements in `nth_column`.
#Overall this is what the function does:The function accepts a 2D list `matrix` and a non-negative integer `n`, and returns the maximum value from the elements at index `n` in each row of `matrix`, provided that `matrix` is not empty, `n` is a valid index, and all elements at index `n` are comparable; otherwise, it may raise a `ValueError` for an empty `matrix`, an `IndexError` for an out-of-range `n`, or a `TypeError` for non-comparable elements.

