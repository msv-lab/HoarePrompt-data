#State of the program right berfore the function call: month is an integer between 1 and 12, inclusive.
def func_1(month):
    months_with_31_days = {1, 3, 5, 7, 8, 10, 12}
    return month in months_with_31_days
    #The program returns True if the month is one of the months with 31 days, which are represented by integers in the set {1, 3, 5, 7, 8, 10, 12}, and False otherwise.
#Overall this is what the function does:Functionality: ** The function accepts an integer `month` representing a month of the year (from 1 to 12) and returns `True` if the month has 31 days (i.e., for the months January, March, May, July, August, October, and December), and `False` otherwise.

