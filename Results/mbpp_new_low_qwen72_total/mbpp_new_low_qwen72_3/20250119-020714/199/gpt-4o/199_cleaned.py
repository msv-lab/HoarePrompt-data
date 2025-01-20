def func_1(n):
    if n < 0:
        return 0
    perrin = [3, 0, 2]
    for i in range(3, n + 1):
        perrin.append(perrin[i - 2] + perrin[i - 3])
    return sum(perrin)
assert func_1(9) == 49
assert func_1(10) == 66
assert func_1(11) == 88