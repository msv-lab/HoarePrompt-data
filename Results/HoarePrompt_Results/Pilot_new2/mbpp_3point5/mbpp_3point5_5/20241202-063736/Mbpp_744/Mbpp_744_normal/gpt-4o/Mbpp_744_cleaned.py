def func_1(tup):
    for item in tup:
        if item is None:
            return True
    return False
assert func_1((10, 4, 5, 6, None)) == True
assert func_1((7, 8, 9, 11, 14)) == False
assert func_1((1, 2, 3, 4, None)) == True