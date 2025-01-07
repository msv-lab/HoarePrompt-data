def func_1(lst):
    return tuple(lst)
assert func_1([5, 10, 7, 4, 15, 3]) == (5, 10, 7, 4, 15, 3)
assert func_1([2, 4, 5, 6, 2, 3, 4, 4, 7]) == (2, 4, 5, 6, 2, 3, 4, 4, 7)
assert func_1([58, 44, 56]) == (58, 44, 56)