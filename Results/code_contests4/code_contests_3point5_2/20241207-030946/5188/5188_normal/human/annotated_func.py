#State of the program right berfore the function call: **
def func_1(a, b):
    if (a > b) :
        return a - b
        #The program returns the result of subtracting integer `b` from integer `a`, where `a` is greater than `b`
    #State of the program after the if block has been executed: a is not greater than b, a and b are variables
    return b - a
    #The program returns the difference between variable b and variable a.
#Overall this is what the function does:The function func_1 accepts two integer parameters a and b. If a is greater than b, it returns the result of subtracting b from a. If b is greater than or equal to a, it returns the result of subtracting a from b.

