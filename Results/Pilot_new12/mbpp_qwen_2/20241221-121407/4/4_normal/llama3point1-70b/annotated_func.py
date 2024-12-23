#State of the program right berfore the function call: num1 and num2 are non-negative integers.
def func_1(num1, num2):
    return bin(num1 ^ num2).count('1') == 1
    #The program returns True if the binary representation of (num1 XOR num2) contains exactly one '1', otherwise it returns False
#Overall this is what the function does:The function `func_1` accepts two non-negative integers `num1` and `num2`. It performs an XOR operation between `num1` and `num2`, converts the result to its binary representation, and checks if this binary string contains exactly one '1'. If the condition is met, the function returns `True`; otherwise, it returns `False`. Potential edge cases include when either `num1` or `num2` is zero, or when both are the same value (resulting in all zeros in the XOR operation). The function does not handle cases where `num1` or `num2` are negative integers, which would result in a TypeError.

