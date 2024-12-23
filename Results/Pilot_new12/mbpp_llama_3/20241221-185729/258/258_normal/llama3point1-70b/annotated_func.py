#State of the program right berfore the function call: num is a non-negative integer.
def func_1(num):
    num_str = str(num)
    num_len = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_len
        
    #State of the program after the  for loop has been executed: `num` is a non-negative integer, `num_str` is the string representation of `num`, `num_len` is the number of digits in `num`, `sum` is the sum of the values of each digit in `num_str` raised to the power of `num_len`, or 0 if `num` is 0.
    return sum == num
    #The program returns True if the sum of the digits of `num` raised to the power of the number of digits in `num` equals `num`, and False otherwise.
#Overall this is what the function does:The function accepts a non-negative integer `num` and returns a boolean value indicating whether the sum of the digits of `num` raised to the power of the number of digits in `num` equals `num`. The function handles all non-negative integers, including 0, and correctly calculates the sum for single-digit and multi-digit numbers. It returns `True` if the sum equals `num`, and `False` otherwise, covering edge cases such as when `num` is 0 or a single-digit number. The function does not modify the input `num` and only uses it to calculate the sum of its digits raised to the power of the number of digits, ensuring that the original value of `num` remains unchanged.

