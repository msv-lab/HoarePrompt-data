#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    num_str = str(n)
    num_len = len(num_str)
    armstrong_sum = sum(int(digit) ** num_len for digit in num_str)
    return armstrong_sum == n
    #`The program returns True if the sum of each digit in 'num_str' raised to the power of 'num_len' is equal to 'n', otherwise it returns False`
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and converts it to a string `num_str`. It then calculates the sum of each digit in `num_str` raised to the power of the length of `num_str`. If this sum equals `n`, the function returns `True`; otherwise, it returns `False`. This process covers all possible non-negative integers, including zero and single-digit numbers. An edge case to note is that for single-digit numbers (0 through 9), the sum of the digit raised to its own power equals the number itself, which is handled correctly by the function.

