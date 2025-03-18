def func_1(numbers):
    return tuple((a * b for (a, b) in zip(numbers, numbers[1:])))