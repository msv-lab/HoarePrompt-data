#State of the program right berfore the function call: month is an integer between 1 and 12, inclusive.
def func_1(month):
    months_with_30_days = {4, 6, 9, 11}
    return month in months_with_30_days
    #The program returns True if the month is in the set of months_with_30_days {4, 6, 9, 11}, otherwise it returns False.
#Overall this is what the function does:The function accepts an integer parameter `month` representing a month of the year (1 for January to 12 for December) and returns `True` if `month` is one of the months with 30 days (April, June, September, November); otherwise, it returns `False`. The function does not handle cases where `month` is outside the range of 1 to 12, as it assumes valid input.

