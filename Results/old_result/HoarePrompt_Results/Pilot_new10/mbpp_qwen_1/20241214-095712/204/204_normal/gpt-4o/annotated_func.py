#State of the program right berfore the function call: month is an integer such that 1 <= month <= 12.
def func_1(month):
    months_with_31_days = {1, 3, 5, 7, 8, 10, 12}
    return month in months_with_31_days
    #`The program returns True if month is 1, 3, 5, 7, 8, 10, or 12, otherwise returns False`
#Overall this is what the function does:The function `func_1` accepts an integer `month` where `1 <= month <= 12` and returns `True` if `month` is one of the following: 1, 3, 5, 7, 8, 10, or 12. Otherwise, it returns `False`.

