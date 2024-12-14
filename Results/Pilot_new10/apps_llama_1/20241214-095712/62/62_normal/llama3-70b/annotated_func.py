#State of the program right berfore the function call: digits is a list of integers and base is an integer such that 2 <= base <= 40 and all elements in digits are between 0 and base-1.
def func_1(digits, base):
    result = 0
    for digit in digits:
        result = result * base + digit
        
    #State of the program after the  for loop has been executed: `digits` is a list of integers, `base` is an integer such that 2 <= `base` <= 40, all elements in `digits` are between 0 and `base`-1, `result` is the decimal equivalent of the number represented by `digits` in base `base`, and if `digits` is not empty, `digit` is the last element in `digits`; otherwise, `result` is 0 if `digits` is empty.
    return result
    #The program returns the decimal equivalent of the number represented by `digits` in base `base`, where `digits` is a list of integers and `base` is an integer between 2 and 40.
#Overall this is what the function does:The function `func_1` accepts a list of integers `digits` and an integer `base`, and returns the decimal equivalent of the number represented by `digits` in base `base`, where `base` is assumed to be between 2 and 40. If `digits` is empty, the function returns 0. The function does not perform any error checking on the input `base`.

