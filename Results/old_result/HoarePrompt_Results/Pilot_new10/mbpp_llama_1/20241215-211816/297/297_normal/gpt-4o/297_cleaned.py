def func_1(t):
    return tuple((t[i] * t[i + 1] for i in range(len(t) - 1)))
assert func_1((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
assert func_1((2, 4, 5, 6, 7)) == (8, 20, 30, 42)
assert func_1((12, 13, 14, 9, 15)) == (156, 182, 126, 135)
assert func_1((12,)) == ()