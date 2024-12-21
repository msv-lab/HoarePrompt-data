#State of the program right berfore the function call: month is an integer between 1 and 12, inclusive.
def func_1(month):
    months_with_30_days = {4, 6, 9, 11}
    return month in months_with_30_days
    #The program returns True if month is an integer in months_with_30_days, which includes 4, 6, 9, and 11; otherwise, it returns False.
#Overall this is what the function does:The function accepts an integer parameter `month`, which is expected to be between 1 and 12, inclusive. It checks if the provided `month` is one of the months with 30 days, specifically April (4), June (6), September (9), or November (11). The function returns `True` if `month` is one of these months; otherwise, it returns `False`. The function properly handles valid inputs within the specified range but does not account for invalid inputs (such as integers outside the range of 1-12) and does not raise any errors if such inputs are provided.

