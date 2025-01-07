def func_1(a, b):
    return (b, a)
assert func_1(10, 20) == (20, 10)
assert func_1(15, 17) == (17, 15)
assert func_1(100, 200) == (200, 100)