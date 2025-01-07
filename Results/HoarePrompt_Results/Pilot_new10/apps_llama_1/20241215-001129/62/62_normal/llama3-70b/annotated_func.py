#State of the program right berfore the function call: digits is a list of non-negative integers, and base is an integer such that 2 ≤ base ≤ 40 and for all i in digits, 0 ≤ digits[i] < base.
def func_1(digits, base):
    result = 0
    for digit in digits:
        result = result * base + digit
        
    #State of the program after the  for loop has been executed: `digits` is a list of non-negative integers, `base` is an integer such that 2 ≤ `base` ≤ 40, for all `i` in `digits`, 0 ≤ `digits[i]` < `base`, and `result` is the decimal equivalent of the base `base` number represented by `digits`.
    return result
    #The program returns the decimal equivalent of the base `base` number represented by `digits`, where `base` is an integer between 2 and 40 (inclusive), and `digits` is a list of non-negative integers each less than `base`.
#Overall this is what the function does:The function accepts a list of integers `digits` and an integer `base`, and returns the decimal equivalent of the base `base` number represented by `digits`. If `digits` is empty, the function returns 0. The function produces a result for any integer `base` and any list of integers `digits`, although the result may not be accurate if `base` is outside the range 2-40 or if `digits` contains negative integers.

