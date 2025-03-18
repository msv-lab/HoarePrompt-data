def func_1(matrix, n):
    nth_column = [row[n] for row in matrix]
    return max(nth_column)
assert func_1([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
assert func_1([[6, 7, 8], [2, 4, 6], [9, 10, 20]], 1) == 10
assert func_1([[7, 8, 9], [3, 5, 7], [10, 11, 21]], 1) == 11