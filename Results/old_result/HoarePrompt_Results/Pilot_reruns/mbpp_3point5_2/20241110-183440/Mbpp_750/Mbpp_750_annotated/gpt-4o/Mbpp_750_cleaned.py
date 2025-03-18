def func_1(lst, tpl):
    return lst + list(tpl)
assert func_1([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
assert func_1([6, 7, 8], (10, 11)) == [6, 7, 8, 10, 11]
assert func_1([7, 8, 9], (11, 12)) == [7, 8, 9, 11, 12]