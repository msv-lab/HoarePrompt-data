def func_1(lst):
    return min(lst)
assert func_1([10, 20, 1, 45, 99]) == 1
assert func_1([1, 2, 3]) == 1
assert func_1([45, 46, 50, 60]) == 45