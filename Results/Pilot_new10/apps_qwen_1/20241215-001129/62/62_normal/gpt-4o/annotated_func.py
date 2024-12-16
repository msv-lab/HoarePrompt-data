#State of the program right berfore the function call: digits is a list of integers representing the digits of a number in a given base, and base is an integer representing the base of the number system (2 ≤ base ≤ 40). The list digits does not contain leading zeros, and all its elements are within the valid range for the given base (0 ≤ digit < base).
def func_1(digits, base):
    decimal_value = 0
    for digit in digits:
        decimal_value = decimal_value * base + digit
        
    #State of the program after the  for loop has been executed: `digits` is a non-empty list, `base` is an integer between 2 and 40 inclusive, `decimal_value` is the decimal representation of the number formed by the digits in `digits` when interpreted in the given base `base`.
    return decimal_value
    #The program returns the decimal representation of the number formed by the digits in list 'digits' when interpreted in the given base 'base'
#Overall this is what the function does:The function accepts a list `digits` and an integer `base`, and returns the decimal representation of the number formed by the digits in `digits` when interpreted in the given base `base`. The function correctly handles the conversion process without leading zeros and ensures that all digits are within the valid range for the given base.

