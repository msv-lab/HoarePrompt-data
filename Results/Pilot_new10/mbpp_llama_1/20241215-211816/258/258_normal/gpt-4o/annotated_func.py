#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    num_str = str(n)
    num_len = len(num_str)
    armstrong_sum = sum(int(digit) ** num_len for digit in num_str)
    return armstrong_sum == n
    #The program returns True if `n` is an Armstrong number (i.e., `n` equals the sum of its digits each raised to the power of the number of digits in `n`), and False otherwise.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns True if `n` is an Armstrong number (i.e., `n` equals the sum of its digits each raised to the power of the number of digits in `n`), and False otherwise.

