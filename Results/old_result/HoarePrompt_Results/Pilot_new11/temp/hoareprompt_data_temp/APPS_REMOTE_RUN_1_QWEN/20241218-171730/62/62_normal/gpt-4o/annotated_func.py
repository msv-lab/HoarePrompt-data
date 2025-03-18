#State of the program right berfore the function call: digits is a list of integers representing the digits of a number in a specific base, and base is an integer representing the base of the number system (2 ≤ base ≤ 40). The list digits does not contain leading zeros, and all elements in digits are non-negative integers less than the base.
def func_1(digits, base):
    decimal_value = 0
    for digit in digits:
        decimal_value = decimal_value * base + digit
        
    #State of the program after the  for loop has been executed: `decimal_value` is the decimal representation of the number formed by the digits in the list `digits` using the specified base, `digits` is a list of integers.
    return decimal_value
    #The program returns `decimal_value` which is the decimal representation of the number formed by the digits in the list `digits` using the specified base
#Overall this is what the function does:The function `func_1` takes a list of integers `digits` and an integer `base`, and converts the number represented by these digits in the given base to its decimal form. The function iterates through each digit in the `digits` list, multiplying the current `decimal_value` by the `base` and adding the current digit to it. After processing all digits, the function returns the `decimal_value` which is the decimal representation of the number. This process handles all digits correctly without leading zeros and ensures that each digit is within the valid range for the given base (0 to base-1). The function does not handle invalid inputs such as a base less than 2 or greater than 40, or non-integer values for `digits` or `base`.

