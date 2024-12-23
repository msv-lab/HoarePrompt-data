def func_1(month: int) -> bool:
    months_with_30_days = {4, 6, 9, 11}
    return month in months_with_30_days
assert func_1(6) == True
assert func_1(2) == False
assert func_1(12) == False