#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    str_n = str(n)
    for digit in str_n:
        if str_n.count(digit) > int(digit):
            return False
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `str_n` is the string representation of `n`, and for every digit in `str_n`, its count in `str_n` is less than or equal to its integer value, unless the function returns False due to this condition being violated.
    return True
    #The program returns True, indicating that for every digit in the string representation of `n`, its count in the string is less than or equal to its integer value.
#Overall this is what the function does:The function accepts a non-negative integer `n`, checks if the count of each digit in the string representation of `n` is less than or equal to its integer value, and returns `True` if this condition holds for all digits; otherwise, it returns `False`.

