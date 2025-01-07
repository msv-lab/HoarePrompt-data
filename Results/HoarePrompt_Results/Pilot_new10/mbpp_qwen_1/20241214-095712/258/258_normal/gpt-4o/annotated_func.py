#State of the program right berfore the function call: n is a positive integer.
def func_1(n):
    num_str = str(n)
    num_len = len(num_str)
    armstrong_sum = sum(int(digit) ** num_len for digit in num_str)
    return armstrong_sum == n
    #`armstrong_sum` is the sum of each digit in `num_str` (the string representation of `n`) raised to the power of `num_len` (the number of digits in `n`), and the program returns whether `armstrong_sum` is equal to `n`
#Overall this is what the function does:The function `func_1` accepts a positive integer `n`, converts it to a string, calculates the sum of each digit raised to the power of the number of digits in `n`, and returns whether this sum is equal to `n`.

