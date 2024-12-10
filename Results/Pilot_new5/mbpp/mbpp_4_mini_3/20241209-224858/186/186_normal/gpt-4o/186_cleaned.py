def func_1(tuple1, tuple2):
    return tuple((a & b for (a, b) in zip(tuple1, tuple2)))
assert func_1((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
assert func_1((1, 2, 3, 4), (5, 6, 7, 8)) == (1, 2, 3, 0)
assert func_1((8, 9, 11, 12), (7, 13, 14, 17)) == (0, 9, 10, 0)