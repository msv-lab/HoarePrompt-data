#State of the program right berfore the function call: num is a non-negative integer.
def func_1(num):
    num_str = str(num)
    num_len = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_len
        
    #State of the program after the  for loop has been executed: `num` is a non-negative integer, `num_str` is the string representation of `num`, `num_len` is the number of digits in `num`, `sum` is equal to the sum of each digit of `num` raised to the power of `num_len`.
    return sum == num
    #The program returns True if sum, which is the sum of each digit of num raised to the power of num_len, is equal to num, indicating that num is a narcissistic number.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `num` as input and checks whether `num` is a narcissistic number. A narcissistic number is defined as a number that is equal to the sum of its digits each raised to the power of the total number of digits in the number. The function does this by converting `num` to a string to extract its digits, calculating the sum of each digit raised to the power of the number of digits, and then comparing this sum to the original number. It returns `True` if `num` is a narcissistic number and `False` otherwise. The function assumes that the input will always be a non-negative integer, so it does not handle negative numbers or non-integer inputs.

