def func_1(month):
    months_with_31_days = {1, 3, 5, 7, 8, 10, 12}
    return month in months_with_31_days
assert func_1(5) == True
assert func_1(2) == False
assert func_1(6) == False
assert func_1(1) == True
assert func_1(12) == True
assert func_1(11) == False