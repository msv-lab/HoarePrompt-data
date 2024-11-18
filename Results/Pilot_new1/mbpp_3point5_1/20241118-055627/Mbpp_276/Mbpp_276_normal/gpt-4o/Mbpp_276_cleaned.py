def func_1(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume
assert math.isclose(func_1(10, 5), 1570.7500000000002, rel_tol=0.001)
assert math.isclose(func_1(4, 5), 251.32000000000002, rel_tol=0.001)
assert math.isclose(func_1(4, 10), 502.64000000000004, rel_tol=0.001)