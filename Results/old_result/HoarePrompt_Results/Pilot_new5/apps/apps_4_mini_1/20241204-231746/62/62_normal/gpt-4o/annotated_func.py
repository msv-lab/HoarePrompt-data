#State of the program right berfore the function call: digits is a list of integers representing the digits of a number in base `base`, where the number of digits is between 1 and 10, and each digit is a non-negative integer less than `base`. The base is an integer between 2 and 40, and the base of X (b_x) is different from the base of Y (b_y).
def func_1(digits, base):
    decimal_value = 0
    for digit in digits:
        decimal_value = decimal_value * base + digit
        
    #State of the program after the  for loop has been executed: `digits` is a list of integers representing the digits of a number in base `base`, `base` is an integer between 2 and 40, `decimal_value` is equal to the decimal representation of the number formed by the digits in `digits` with respect to the provided base.
    return decimal_value
    #The program returns the decimal representation of the number formed by the digits in 'digits' with respect to the provided base, which is stored in 'decimal_value'
#Overall this is what the function does:The function accepts a list of integers `digits`, which represent the digits of a number in a specified base (which must be between 2 and 40), and an integer `base`. It calculates and returns the decimal representation of the number formed by those digits in the provided base. The function assumes that all digits are valid for the given base and that the list contains between 1 and 10 digits. No error handling for invalid digits (digits that are not less than the base) is included, which could lead to incorrect results if such cases arise.

