#State of the program right berfore the function call: n is an integer such that 1 <= n <= 12, representing a month of the year.
def func_1(n):
    months_31_days = [1, 3, 5, 7, 8, 10, 12]
    return n in months_31_days
    #The program returns True if the month corresponding to `n` has 31 days, False otherwise
#Overall this is what the function does:The function accepts an integer `n` representing a month of the year and returns `True` if the month has 31 days (January, March, May, July, August, October, and December), and `False` otherwise (February, April, June, September, and November).

