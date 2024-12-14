#State of the program right berfore the function call: num is an integer.
def func_1(num):
    num_str = str(num)
    num_len = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_len
        
    #State of the program after the  for loop has been executed: `num` is an integer, `num_str` is a string representation of `num`, `num_len` is the length of `num_str`, `sum` is the sum of each digit in `num_str` raised to the power of `num_len`.
    return sum == num
    #The program returns True if the sum of each digit in `num_str` raised to the power of `num_len` equals `num`, otherwise it returns False
#Overall this is what the function does:The function accepts an integer `num`, converts it to a string, and calculates the sum of each digit in the string representation of `num` raised to the power of the length of the string. If the calculated sum equals `num`, it returns `True`; otherwise, it returns `False`.

