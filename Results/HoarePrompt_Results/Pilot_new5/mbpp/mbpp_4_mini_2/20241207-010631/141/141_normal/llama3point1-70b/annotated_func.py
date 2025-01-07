#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    str_n = str(n)
    for digit in str_n:
        if str_n.count(digit) > int(digit):
            return False
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `str_n` is the string representation of `n`, and for every character `digit` in `str_n`, the count of `digit` in `str_n` is less than or equal to the integer value of `digit`. If any count exceeds, the function would have returned False, indicating an invalid state.
    return True
    #The program returns True, indicating that the count of each digit in the string representation of n is less than or equal to the integer value of that digit, confirming a valid state.
#Overall this is what the function does:The function accepts a non-negative integer `n`, and returns `False` if any digit in its string representation appears more times than its integer value; otherwise, it returns `True`. It will also return `True` for the case when `n` is 0.

