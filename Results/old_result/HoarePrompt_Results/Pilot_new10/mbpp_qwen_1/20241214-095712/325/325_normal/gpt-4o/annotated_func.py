#State of the program right berfore the function call: month is an integer such that 1 <= month <= 12.
def func_1(month):
    months_with_30_days = {4, 6, 9, 11}
    return month in months_with_30_days
    #The program returns True if month is 4, 6, 9, or 11, otherwise returns False
#Overall this is what the function does:The function accepts an integer `month` (1 ≤ month ≤ 12) and returns `True` if the month has 30 days, specifically if the month is 4, 6, 9, or 11. If the month does not match any of these, it returns `False`.

