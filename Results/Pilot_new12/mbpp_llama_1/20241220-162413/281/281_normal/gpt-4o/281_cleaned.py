def func_1(numbers):
    return [num for num in numbers if num % 2 == 0]
assert func_1([1, 2, 3, 4, 5]) == [2, 4]
assert func_1([4, 5, 6, 7, 8, 0, 1]) == [4, 6, 8, 0]
assert func_1([8, 12, 15, 19]) == [8, 12]