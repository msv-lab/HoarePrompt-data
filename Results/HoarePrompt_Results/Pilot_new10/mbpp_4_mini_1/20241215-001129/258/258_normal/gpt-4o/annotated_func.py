#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    num_str = str(n)
    num_len = len(num_str)
    armstrong_sum = sum(int(digit) ** num_len for digit in num_str)
    return armstrong_sum == n
    #The program returns whether the sum of each digit in `num_str` raised to the power of `num_len` is equal to the original non-negative integer `n`.
#Overall this is what the function does:The function accepts a non-negative integer `n` and checks if it is an Armstrong number. It calculates the sum of each digit of `n` raised to the power of the number of digits in `n`, and returns `True` if this sum equals `n`, and `False` otherwise. The function correctly handles any non-negative integer, including single-digit numbers which are always Armstrong numbers.

