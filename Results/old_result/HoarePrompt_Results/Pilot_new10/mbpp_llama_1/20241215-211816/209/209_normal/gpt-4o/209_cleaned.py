def func_1(lst):
    return [sublist[0] for sublist in lst]
assert func_1([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
assert func_1([[1, 2, 3], [4, 5]]) == [1, 4]
assert func_1([[9, 8, 1], [1, 2]]) == [9, 1]