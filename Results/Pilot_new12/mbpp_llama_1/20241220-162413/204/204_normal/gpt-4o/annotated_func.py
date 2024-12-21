#State of the program right berfore the function call: month is an integer such that 1 <= month <= 12.
def func_1(month):
    months_with_31_days = {1, 3, 5, 7, 8, 10, 12}
    return month in months_with_31_days
    #The program returns True if the month has 31 days (January, March, May, July, August, October, December) and False otherwise (February, April, June, September, November)
#Overall this is what the function does:The function determines whether a given month has 31 days, returning True for months with 31 days (January, March, May, July, August, October, December) and False for months with fewer days (February, April, June, September, November). It accepts an integer month as input, where 1 <= month <= 12, and returns a boolean value indicating whether the month has 31 days. The function does not handle cases where the input month is outside the specified range (i.e., month < 1 or month > 12), which may result in undefined behavior. The function's primary purpose is to categorize months based on the number of days they contain, specifically identifying those with 31 days.

