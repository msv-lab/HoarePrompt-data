#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    str_n = str(n)
    for digit in str_n:
        if str_n.count(digit) > int(digit):
            return False
        
    #State of the program after the  for loop has been executed: `str_n` is a string with at least one character, and for every digit in `str_n`, the count of that digit in `str_n` is less than or equal to the integer value of the next character in `str_n`. If any digit's count in `str_n` is greater than the integer value of the next character in `str_n`, the function returns False. Otherwise, the function returns None.
    return True
    #The program returns True
#Overall this is what the function does:The function accepts a non-negative integer `n`, converts it to a string, and returns `True` if the count of any digit in the string is not greater than the integer value of the next digit. Otherwise, it returns `False`.

