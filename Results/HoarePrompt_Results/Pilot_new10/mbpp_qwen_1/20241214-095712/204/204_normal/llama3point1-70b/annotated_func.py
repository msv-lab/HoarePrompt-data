#State of the program right berfore the function call: n is an integer such that 1 <= n <= 12.
def func_1(n):
    months_31_days = [1, 3, 5, 7, 8, 10, 12]
    return n in months_31_days
    #The program returns True if n is in the list [1, 3, 5, 7, 8, 10, 12], otherwise returns False
#Overall this is what the function does:The function `func_1` accepts an integer `n` in the range 1 to 12 and returns `True` if `n` is in the list `[1, 3, 5, 7, 8, 10, 12]`, otherwise it returns `False`.

