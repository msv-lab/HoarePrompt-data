#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    num_str = str(n)
    num_len = len(num_str)
    armstrong_sum = sum(int(digit) ** num_len for digit in num_str)
    return armstrong_sum == n
    #The program returns whether the sum of each digit of n raised to the power of the number of digits in n is equal to n.
#Overall this is what the function does:The function accepts a non-negative integer `n`, converts it to its string representation, and calculates the sum of each digit raised to the power of the total number of digits in `n`. It then checks whether this sum is equal to the original number `n`. This function effectively checks if `n` is an Armstrong number (or narcissistic number). The function always returns a boolean value: `True` if `n` is an Armstrong number and `False` otherwise. It does not handle negative integers or non-integer inputs, as it explicitly assumes `n` is a non-negative integer.

