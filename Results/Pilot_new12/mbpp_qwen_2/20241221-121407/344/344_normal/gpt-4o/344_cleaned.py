def func_1(sorted_list, value):
    return bisect.bisect_right(sorted_list, value)
assert func_1([1, 2, 4, 5], 6) == 4
assert func_1([1, 2, 4, 5], 3) == 2
assert func_1([1, 2, 4, 5], 7) == 4