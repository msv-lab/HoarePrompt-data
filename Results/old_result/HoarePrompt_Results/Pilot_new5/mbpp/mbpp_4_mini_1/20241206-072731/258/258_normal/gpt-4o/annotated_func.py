#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    num_str = str(n)
    num_len = len(num_str)
    armstrong_sum = sum(int(digit) ** num_len for digit in num_str)
    return armstrong_sum == n
    #The program returns True if armstrong_sum, which is the sum of each digit of the string representation of n raised to the power of its length, equals n; otherwise, it returns False.
#Overall this is what the function does:The function accepts a non-negative integer `n` and checks if it is an Armstrong number, returning True if it is and False otherwise. An Armstrong number (or narcissistic number) for a given number of digits is a number that is equal to the sum of its digits each raised to the power of the number of digits. The function does not handle any input validation, so passing negative integers or non-integer types would lead to unexpected behavior or errors.

