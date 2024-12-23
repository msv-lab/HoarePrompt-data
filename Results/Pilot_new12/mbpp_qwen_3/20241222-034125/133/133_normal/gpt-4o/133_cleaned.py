def func_1(tup1, tup2):
    return tuple((a - b for (a, b) in zip(tup1, tup2)))
assert func_1((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
assert func_1((11, 2, 3), (24, 45, 16)) == (-13, -43, -13)
assert func_1((7, 18, 9), (10, 11, 12)) == (-3, 7, -3)