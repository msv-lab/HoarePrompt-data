#State of the program right berfore the function call: digits is a list of non-negative integers, and base is an integer between 2 and 40 (inclusive), where each digit in digits is less than base.
def func_1(digits, base):
    decimal_value = 0
    for digit in digits:
        decimal_value = decimal_value * base + digit
        
    #State of the program after the  for loop has been executed: `digits` is a list of non-negative integers, each less than `base`, `base` is an integer between 2 and 40 (inclusive), and `decimal_value` is the decimal equivalent of the number represented by the original list `digits` in base `base`.
    return decimal_value
    #The program returns the decimal equivalent of the number represented by the list `digits` in base `base`, where `base` is an integer between 2 and 40 (inclusive) and `digits` is a list of non-negative integers each less than `base`.
#Overall this is what the function does:The function accepts a list of non-negative integers `digits` and an integer `base`, calculates and returns the decimal equivalent of the number represented by `digits` in base `base` without any error checking or handling, regardless of whether `base` is between 2 and 40 or each digit in `digits` is less than `base`.

