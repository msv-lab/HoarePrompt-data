def func_1(num):
    return cmath.polar(complex(num))
assert func_1(1) == (1.0, 0.0)
assert func_1(4) == (4.0, 0.0)
assert func_1(5) == (5.0, 0.0)