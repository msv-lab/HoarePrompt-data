#State of the program right berfore the function call: num is a non-negative integer.
def func_1(num):
    num_str = str(num)
    num_len = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_len
        
    #State of the program after the  for loop has been executed: `num` is a non-negative integer, `sum` is equal to the sum of each digit of `num` raised to the power of the length of `num_str`, `num_len` is the length of `num_str`.
    return sum == num
    #The program returns whether 'sum' is equal to 'num', where 'sum' is the sum of each digit of 'num' raised to the power of the length of 'num_str', and 'num_len' is the length of 'num_str'.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `num` and checks whether it is an Armstrong number. It calculates the sum of each digit of `num`, each raised to the power of the total number of digits in `num`. The function returns `True` if this calculated sum is equal to `num`, and `False` otherwise. It is assumed that the input `num` is a valid non-negative integer, but the function does not handle invalid inputs or negative values.

