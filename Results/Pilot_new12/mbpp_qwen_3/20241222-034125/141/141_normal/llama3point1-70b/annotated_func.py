#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    str_n = str(n)
    for digit in str_n:
        if str_n.count(digit) > int(digit):
            return False
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `str_n` is an empty string, and the function returns True.
    return True
    #The program returns True
#Overall this is what the function does:-

