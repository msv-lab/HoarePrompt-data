#State of the program right berfore the function call: month is an integer between 1 and 12 inclusive.
def func_1(month):
    months_with_30_days = {4, 6, 9, 11}
    return month in months_with_30_days
    #The program returns True if 'month' is in the set {4, 6, 9, 11}, indicating that 'month' has 30 days, otherwise it returns False.
#Overall this is what the function does:The function accepts an integer `month` (between 1 and 12 inclusive) and returns `True` if `month` corresponds to April (4), June (6), September (9), or November (11), indicating that those months have 30 days. It returns `False` for all other months, including those with 31 days and February, which has 28 or 29 days.

