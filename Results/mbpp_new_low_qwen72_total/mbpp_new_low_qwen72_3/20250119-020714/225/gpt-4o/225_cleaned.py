def func_1(n):
    sum_n = n * (n + 1) // 2
    sum_cubes_n = sum_n ** 2
    return sum_cubes_n - sum_n
assert func_1(3) == 30
assert func_1(5) == 210
assert func_1(2) == 6