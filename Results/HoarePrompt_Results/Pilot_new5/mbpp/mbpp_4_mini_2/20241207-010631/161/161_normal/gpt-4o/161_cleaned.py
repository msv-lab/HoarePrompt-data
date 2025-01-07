def func_1(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        (a, b) = (2, 1)
        for _ in range(2, n + 1):
            (a, b) = (b, a + b)
        return b
assert func_1(9) == 76
assert func_1(4) == 7
assert func_1(3) == 4