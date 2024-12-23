#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    num_str = str(n)
    num_len = len(num_str)
    armstrong_sum = sum(int(digit) ** num_len for digit in num_str)
    return armstrong_sum == n
    #`The program returns True if the sum of the digits of `num_str` each raised to the power of `num_len` is equal to `n`, otherwise it returns False`
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and checks whether the sum of its digits each raised to the power of the number of digits equals `n`. If this condition is met, it returns `True`; otherwise, it returns `False`. Potential edge cases include when `n` is 0 (which is an Armstrong number), or when `n` is a single-digit number (as the sum of a single digit raised to the power of 1 is the digit itself). The function correctly handles these cases and no additional functionality is missing.

