#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    num_str = str(n)
    num_len = len(num_str)
    armstrong_sum = sum(int(digit) ** num_len for digit in num_str)
    return armstrong_sum == n
    #The program returns True if `n` is an Armstrong number (i.e., the sum of its digits each raised to the power of the number of digits equals `n`), and False otherwise.
#Overall this is what the function does:The function determines whether a given non-negative integer `n` is an Armstrong number, returning `True` if the sum of its digits each raised to the power of the number of digits equals `n`, and `False` otherwise, covering all potential cases including single-digit numbers, multi-digit numbers, and edge cases where `n` is 0.

