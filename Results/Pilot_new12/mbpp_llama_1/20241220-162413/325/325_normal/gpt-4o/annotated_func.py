#State of the program right berfore the function call: month is an integer such that 1 <= month <= 12.
def func_1(month):
    months_with_30_days = {4, 6, 9, 11}
    return month in months_with_30_days
    #The program returns True if the month is one of {4, 6, 9, 11} and False otherwise
#Overall this is what the function does:The function determines whether a given month has 30 days, returning True if the month is April, June, September, or November, and False otherwise. It accepts a single integer parameter representing the month, where 1 <= month <= 12. The function does not modify the input month and only returns a boolean value indicating whether the month has 30 days. It handles all possible month values within the valid range, but does not include any error checking or handling for invalid month values outside of this range.

