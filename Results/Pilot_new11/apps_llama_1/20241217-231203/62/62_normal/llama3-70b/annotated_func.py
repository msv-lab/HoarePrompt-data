#State of the program right berfore the function call: digits is a list of integers and base is an integer such that 2 <= base <= 40 and all elements in digits are between 0 and base - 1.
def func_1(digits, base):
    result = 0
    for digit in digits:
        result = result * base + digit
        
    #State of the program after the  for loop has been executed: `result` is the base 10 equivalent of the number represented by `digits` in base `base`, `base` is an integer between 2 and 40 (inclusive), and all elements in `digits` are between 0 and `base` - 1. If `digits` is empty, `result` is 0.
    return result
    #The program returns the base 10 equivalent of the number represented by `digits` in base `base`, which is an integer between 2 and 40 (inclusive), or 0 if `digits` is empty
#Overall this is what the function does:The function converts a number represented by a list of digits in a given base to its base 10 equivalent. It accepts a list of integers `digits` and an integer `base` as input, where `base` is between 2 and 40 (inclusive) and all elements in `digits` are between 0 and `base - 1`. The function returns an integer representing the base 10 equivalent of the input number. If the input list `digits` is empty, the function returns 0. The function handles all potential edge cases, including an empty input list and inputs with varying lengths and values, and it does not modify the input parameters `digits` and `base`. The function performs the conversion by iteratively multiplying the current result by the base and adding the next digit, effectively calculating the base 10 equivalent of the input number.

