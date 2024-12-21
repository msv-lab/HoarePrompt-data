#State of the program right berfore the function call: num is a non-negative integer.
def func_1(num):
    num_str = str(num)
    num_len = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_len
        
    #State of the program after the  for loop has been executed: `num` is a non-negative integer, `num_str` is the string representation of `num`, `num_len` is the number of digits in `num`, and `sum` is the sum of each digit in `num` raised to the power of `num_len`.
    return sum == num
    #The program returns a boolean value indicating whether the sum of each digit in `num` raised to the power of the number of digits in `num` is equal to `num` itself.
#Overall this is what the function does:The function accepts a non-negative integer parameter `num` and returns a boolean value indicating whether the sum of each digit in `num` raised to the power of the number of digits in `num` equals `num`. The function handles all potential edge cases, including when `num` is 0 (in which case it returns True because 0^1 = 0) and when `num` is a single-digit number (where it correctly calculates the power). The function also correctly handles multi-digit numbers by iterating over each digit, raising it to the power of the total number of digits, and summing these values for comparison with the original number. Note that the input `num` itself remains unchanged throughout the execution of the function, as the function only operates on its string representation and calculated values. The return value is a boolean (True or False) based on whether the calculated sum equals the original input `num`.

