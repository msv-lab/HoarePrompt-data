#State of the program right berfore the function call: month is an integer such that 1 <= month <= 12.
def func_1(month):
    thirty_days_months = [4, 6, 9, 11]
    return month in thirty_days_months
    #The program returns True if the month is one of the months with 30 days (April, June, September, November), and False otherwise.
#Overall this is what the function does:The function accepts an integer month and returns True if the month is April, June, September, or November, and False otherwise, effectively identifying months with 30 days in the standard Gregorian calendar.

