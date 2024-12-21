#State of the program right berfore the function call: num is a non-negative integer.
def func_1(num):
    num_str = str(num)
    num_len = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_len
        
    #State of the program after the  for loop has been executed: `num` is a non-negative integer, `num_str` represents `num`, `num_len` is the number of digits in `num`, and `sum` is the sum of each digit in `num` raised to the power of `num_len`.
    return sum == num
    #The program returns True if 'sum', which is the sum of each digit in 'num' raised to the power of 'num_len', equals 'num'; otherwise, it returns False.
#Overall this is what the function does:The function accepts a non-negative integer `num` and checks whether it is a "Narcissistic number" (also known as an Armstrong number). It computes the sum of each digit of `num` raised to the power of the total number of digits in `num`. The function returns `True` if this sum equals `num`, indicating that `num` is a Narcissistic number. If the computed sum does not equal `num`, the function returns `False`. Therefore, the function effectively identifies Narcissistic numbers among non-negative integers. Note that potential edge cases, such as single-digit numbers (which are always Narcissistic), are handled since each digit raised to the power of one equals the digit itself.

