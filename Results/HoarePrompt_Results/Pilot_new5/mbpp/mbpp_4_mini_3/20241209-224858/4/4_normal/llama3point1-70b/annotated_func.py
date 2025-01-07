#State of the program right berfore the function call: num1 and num2 are non-negative integers.
def func_1(num1, num2):
    return bin(num1 ^ num2).count('1') == 1
    #The program returns True if num1 and num2 differ by exactly one bit in their binary representation, otherwise it returns False.
#Overall this is what the function does:The function accepts two non-negative integers, `num1` and `num2`, and returns True if they differ by exactly one bit in their binary representation; otherwise, it returns False. This includes cases where both numbers are zero, in which case the function will return False, as they do not differ by any bits.

