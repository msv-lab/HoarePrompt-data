#State of the program right berfore the function call: **
def func_1(c, d):
    if (c >= 0) :
        return c / d
        #The program returns the result of dividing the integer `c` by the variable `d`.
    #State of the program after the if block has been executed: *c is an integer. c is less than 0
    return c / d
    #The program returns the result of dividing the integer c (which is less than 0) by the variable d.
#Overall this is what the function does:The function `func_1` accepts two parameters `c` and `d`, both of which are integers. The function then returns the result of dividing `c` by `d`, regardless of the value of `c`. If `c` is negative, the function still performs the division and returns the result.

