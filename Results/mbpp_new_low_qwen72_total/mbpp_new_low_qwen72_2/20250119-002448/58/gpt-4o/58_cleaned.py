def func_1(bool_list):
    return sum(bool_list)
assert func_1([True, False, True]) == 2
assert func_1([False, False]) == 0
assert func_1([True, True, True]) == 3