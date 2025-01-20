def func_1(lst):
    int_values = [x for x in lst if isinstance(x, int)]
    return min(int_values)
assert func_1(['Python', 3, 2, 4, 5, 'version']) == 2
assert func_1(['Python', 15, 20, 25]) == 15
assert func_1(['Python', 30, 20, 40, 50, 'version']) == 20