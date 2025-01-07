#State of the program right berfore the function call: num is a non-negative integer.
def func_1(num):
    num_str = str(num)
    num_len = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_len
        
    #State of the program after the  for loop has been executed: `num` is a non-negative integer (≥ 0), `num_str` is the string representation of `num`, `num_len` is the number of digits in `num`, `sum` is equal to the sum of each integer value of the digits in `num_str` raised to the power of `num_len`.
    return sum == num
    #The program returns whether 'sum' is equal to 'num', where 'sum' is the sum of each digit of 'num' raised to the power of 'num_len', and 'num_len' is the number of digits in 'num'.
#Overall this is what the function does:The function accepts a non-negative integer `num` and returns `True` if `num` is an Armstrong number; that is, if the sum of its digits each raised to the power of the total number of digits equals `num`. If this condition is not satisfied, it returns `False`.

