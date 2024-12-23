def func_1(lst):
    return sum(set(lst))
assert func_1([1, 2, 3, 1, 1, 4, 5, 6]) == 21
assert func_1([1, 10, 9, 4, 2, 10, 10, 45, 4]) == 71
assert func_1([12, 10, 9, 45, 2, 10, 10, 45, 10]) == 78