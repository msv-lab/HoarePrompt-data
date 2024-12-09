#State of the program right berfore the function call: month is an integer in the range from 1 to 12, inclusive.
def func_1(month):
    months_with_30_days = {4, 6, 9, 11}
    return month in months_with_30_days
    #The program returns True if month is in the set of months_with_30_days {4, 6, 9, 11}, otherwise it returns False.
#Overall this is what the function does:The function accepts an integer `month` and returns True if it corresponds to a month with 30 days (April, June, September, November); otherwise, it returns False.

