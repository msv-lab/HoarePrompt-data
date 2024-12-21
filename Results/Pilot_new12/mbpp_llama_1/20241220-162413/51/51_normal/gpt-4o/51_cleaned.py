def func_1(numbers):
    product = 1
    for num in numbers:
        product *= num
    result = product / len(numbers)
    return result
assert math.isclose(func_1((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
assert math.isclose(func_1((-10, -20, -30)), -2000.0, rel_tol=0.001)
assert math.isclose(func_1((19, 15, 18)), 1710.0, rel_tol=0.001)