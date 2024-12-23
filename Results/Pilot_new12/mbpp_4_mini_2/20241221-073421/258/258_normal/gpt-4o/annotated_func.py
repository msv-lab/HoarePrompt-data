#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    num_str = str(n)
    num_len = len(num_str)
    armstrong_sum = sum(int(digit) ** num_len for digit in num_str)
    return armstrong_sum == n
    #The program returns a boolean indicating whether armstrong_sum, which is the sum of each digit in num_str raised to the power of num_len, is equal to n, where n is a non-negative integer.
#Overall this is what the function does:The function accepts a non-negative integer `n` and checks whether `n` is an Armstrong number. An Armstrong number (or Narcissistic number) for a given number of digits is a number that is equal to the sum of its own digits each raised to the power of the number of digits. The function converts `n` to a string to access its digits, computes the number of digits, calculates the sum of each digit raised to the power of the total count of digits, and returns a boolean indicating if this sum equals `n`. It correctly handles all non-negative integers, including 0 and single-digit numbers, as they qualify as Armstrong numbers. The boolean result indicates whether the input `n` meets the Armstrong criteria.

