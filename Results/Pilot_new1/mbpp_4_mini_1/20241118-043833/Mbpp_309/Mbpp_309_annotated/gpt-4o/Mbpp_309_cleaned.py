def func_1(a, b):
    return a if a > b else b
assert func_1(5, 10) == 10
assert func_1(-1, -2) == -1
assert func_1(9, 7) == 9