def func_1(n):
    natural_numbers = range(1, n + 1)
    cubes = [x ** 3 for x in natural_numbers]
    sum_of_cubes = sum(cubes)
    average = sum_of_cubes / n
    return average
assert func_1(2) == 4.5
assert func_1(3) == 12
assert func_1(1) == 1