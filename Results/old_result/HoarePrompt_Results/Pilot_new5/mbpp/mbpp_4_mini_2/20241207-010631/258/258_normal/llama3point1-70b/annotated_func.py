#State of the program right berfore the function call: num is a non-negative integer.
def func_1(num):
    num_str = str(num)
    num_len = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_len
        
    #State of the program after the  for loop has been executed: `num` is a non-negative integer, `num_str` is a non-empty string, `num_len` equals the length of `num_str`, `sum` is equal to the sum of each digit in `num_str` raised to the power of `num_len`.
    return sum == num
    #The program returns True if the sum of each digit in 'num_str' raised to the power of 'num_len' is equal to 'num', otherwise it returns False.
#Overall this is what the function does:The function accepts a non-negative integer `num` and returns True if `num` is an Armstrong number (i.e., the sum of its digits each raised to the power of the number of digits equals `num`), and False otherwise. It does not handle negative integers or non-integer inputs, as it assumes `num` is always a non-negative integer.

