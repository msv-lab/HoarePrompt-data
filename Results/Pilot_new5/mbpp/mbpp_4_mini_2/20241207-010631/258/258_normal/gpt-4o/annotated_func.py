#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    num_str = str(n)
    num_len = len(num_str)
    armstrong_sum = sum(int(digit) ** num_len for digit in num_str)
    return armstrong_sum == n
    #The program returns a boolean value indicating whether the sum of each digit of the non-negative integer 'n', raised to the power of the number of digits in 'n', is equal to 'n' itself.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns `True` if `n` is an Armstrong number (i.e., if the sum of its digits each raised to the power of the number of digits equals `n`); otherwise, it returns `False`. It correctly handles all non-negative integers, including `0`.

