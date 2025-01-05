#State of the program right berfore the function call: **Precondition**: **a and b are integers such that 2 <= a, b <= 109. x1, y1, x2, y2 are integers such that |x1|,|y1|,|x2|,|y2| <= 109.**
def func_1(c, d):
    if (c >= 0) :
        return c / d
        #The program returns the division of integer c by an unknown variable d
    #State of the program after the if block has been executed: *a and b are integers such that 2 <= a, b <= 109. x1, y1, x2, y2 are integers such that |x1|,|y1|,|x2|,|y2| <= 109. c is an integer such that c < 0.
    return c / d
    #The program returns the result of dividing integer 'c' by integer 'd'
#Overall this is what the function does:The function `func_1` accepts two integer parameters `c` and `d`. It returns the division of `c` by `d` in all cases, despite the annotations suggesting otherwise. Therefore, the actual functionality of the function is to always return the result of dividing `c` by `d`.

