#State of the program right berfore the function call: n is a non-negative integer.**
def func_1(n):
    if (n < 2) :
        return n
        #The program returns the current value of n, which is a non-negative integer. If n is less than 2, then the current value of n is less than 2
    else :
        if (n == 2 or n == 3) :
            return n
            #The program returns the non-negative integer value of `n`, which is either 2 or 3
        else :
            if (n == 4) :
                return 4
                #The program returns the integer 4
            else :
                return 0
                #The program returns 0
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and returns different values based on the conditions specified for each case. If `n` is less than 2, the function returns the current value of `n`. If `n` is either 2 or 3, the function returns `n`. If `n` is 4, the function returns 4. If none of these conditions are met, the function returns 0.

