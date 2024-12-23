#State of the program right berfore the function call: digits is a list of integers representing the digits of a number, base is an integer representing the base of the number where 2 ≤ base ≤ 40 and all digits are non-negative and less than the base.
def func_1(digits, base):
    decimal_value = 0
    for digit in digits:
        decimal_value = decimal_value * base + digit
        
    #State of the program after the  for loop has been executed: `digits` is a list of integers representing digits in a number, `base` is an integer in the range [2, 40], `decimal_value` is equal to the decimal equivalent of the number represented by `digits` in the given `base`.
    return decimal_value
    #The program returns decimal_value, which is the decimal equivalent of the number represented by the list of integers 'digits' in the given 'base' within the range [2, 40].
#Overall this is what the function does:The function accepts a list of integers `digits`, which represents the digits of a number, and an integer `base` within the range [2, 40]. It calculates and returns the decimal equivalent of the number represented by the `digits` in the specified `base`. The function assumes that all digits in the list are non-negative and less than the base. It does not handle cases where the input digits contain invalid values (i.e., digits not less than the base) or cases where the inputs could be empty. After the function concludes, it returns `decimal_value`, which is the computed decimal equivalent of the number represented by `digits`.

