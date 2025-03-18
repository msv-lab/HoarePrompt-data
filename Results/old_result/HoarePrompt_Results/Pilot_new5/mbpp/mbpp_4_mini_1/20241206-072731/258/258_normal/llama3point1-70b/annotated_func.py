#State of the program right berfore the function call: num is a non-negative integer.
def func_1(num):
    num_str = str(num)
    num_len = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_len
        
    #State of the program after the  for loop has been executed: `num` is a non-negative integer, `num_str` is a string representation of `num`, `num_len` is the length of `num_str`, `sum` is equal to the sum of each digit in `num_str` raised to the power of `num_len`.
    return sum == num
    #The program returns True if the sum of each digit in the string representation of the non-negative integer num, raised to the power of the length of that string, equals num; otherwise, it returns False.
#Overall this is what the function does:The function accepts a non-negative integer `num` and checks if it is an Armstrong number. It calculates the sum of each digit in `num`, raised to the power of the number of digits in `num`. The function returns `True` if this sum equals `num`; otherwise, it returns `False`.

