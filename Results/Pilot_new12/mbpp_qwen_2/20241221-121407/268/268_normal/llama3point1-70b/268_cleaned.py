def func_1(matrix, n):
    return max((row[n - 1] for row in matrix))