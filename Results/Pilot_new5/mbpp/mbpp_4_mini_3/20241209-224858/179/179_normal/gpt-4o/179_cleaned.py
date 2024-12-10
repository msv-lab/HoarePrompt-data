def func_1(n):
    even_numbers = [2 * i for i in range(1, n + 1)]
    cube_sum = sum((x ** 3 for x in even_numbers))
    return cube_sum
assert func_1(2) == 72
assert func_1(3) == 288
assert func_1(4) == 800