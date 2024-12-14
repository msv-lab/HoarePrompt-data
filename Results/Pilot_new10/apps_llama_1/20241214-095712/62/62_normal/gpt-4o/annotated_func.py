#State of the program right berfore the function call: digits is a list of non-negative integers, and base is an integer such that 2 ≤ base ≤ 40, and for all i in digits, 0 ≤ digits[i] < base.
def func_1(digits, base):
    decimal_value = 0
    for digit in digits:
        decimal_value = decimal_value * base + digit
        
    #State of the program after the  for loop has been executed: `decimal_value` is the decimal representation of the number formed by `digits` in base `base`, `base` is an integer such that 2 ≤ `base` ≤ 40, and `digits` is a list of non-negative integers less than `base`.
    return decimal_value
    #The program returns decimal_value, the decimal representation of the number formed by `digits` in base `base`, where `base` is an integer between 2 and 40 (inclusive) and `digits` is a list of non-negative integers less than `base`.
#Overall this is what the function does:The function accepts a list of non-negative integers `digits` and an integer `base`, and returns the decimal representation of the number formed by `digits` in base `base`, assuming `digits` and `base` are valid inputs, and handling cases where `digits` might be empty or `base` might be outside the range of 2 to 40, in which case it still computes a decimal value based on the given inputs without validation.

