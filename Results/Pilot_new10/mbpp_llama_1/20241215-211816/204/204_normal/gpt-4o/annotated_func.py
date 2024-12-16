#State of the program right berfore the function call: month is an integer such that 1 <= month <= 12.
def func_1(month):
    months_with_31_days = {1, 3, 5, 7, 8, 10, 12}
    return month in months_with_31_days
    #The program returns True if the month has 31 days (January, March, May, July, August, October, December) and False otherwise (February, April, June, September, November)
#Overall this is what the function does:The function accepts an integer month between 1 and 12 and returns True if the month has 31 days (January, March, May, July, August, October, December) and False otherwise.

