def func_1(lst):
    return sum((1 for x in lst if isinstance(x, int)))
assert func_1([1, 2, 'abc', 1.2]) == 2
assert func_1([1, 2, 3]) == 3
assert func_1([1, 1.2, 4, 5.1]) == 2