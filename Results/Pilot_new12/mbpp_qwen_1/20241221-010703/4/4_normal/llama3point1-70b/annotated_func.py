#State of the program right berfore the function call: num1 and num2 are non-negative integers.
def func_1(num1, num2):
    return bin(num1 ^ num2).count('1') == 1
    #The program returns True if the number of '1's in the binary representation of (num1 XOR num2) is exactly 1, otherwise it returns False
#Overall this is what the function does:The function `func_1` accepts two non-negative integers `num1` and `num2`. It performs a bitwise XOR operation on `num1` and `num2`, converts the result to its binary representation, counts the number of '1's in this binary string, and returns `True` if the count is exactly 1, otherwise it returns `False`. The function handles all valid inputs within the specified domain (non-negative integers) and correctly evaluates the XOR result for all such inputs.

