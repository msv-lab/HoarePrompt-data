def func_1(base, height, length):
    base_area = 0.5 * base * height
    volume = base_area * length
    return volume
assert func_1(10, 8, 6) == 240
assert func_1(3, 2, 2) == 6
assert func_1(1, 2, 1) == 1