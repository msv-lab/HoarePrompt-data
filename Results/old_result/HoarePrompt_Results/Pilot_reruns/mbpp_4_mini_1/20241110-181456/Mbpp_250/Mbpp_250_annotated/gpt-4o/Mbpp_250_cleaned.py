def func_1(tup, element):
    return tup.count(element)
assert func_1((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4) == 0
assert func_1((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 10) == 3
assert func_1((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 8) == 4