#State of the program right berfore the function call: digits is a list of non-negative integers and base is an integer such that 2 <= base <= 40, and all elements in digits are less than base.
def func_1(digits, base):
    decimal_value = 0
    for digit in digits:
        decimal_value = decimal_value * base + digit
        
    #State of the program after the  for loop has been executed: `digits` is a list of non-negative integers, `base` is an integer such that 2 <= `base` <= 40, all elements in `digits` are less than `base`, and `decimal_value` is the decimal value of the number represented by the digits in the list with the given base, if the list is empty `decimal_value` is 0.
    return decimal_value
    #The program returns the decimal value of the number represented by the digits in the list with the given base, where the list of digits are non-negative integers less than the base, and the base is an integer between 2 and 40, if the list is empty the returned decimal value is 0
#Overall this is what the function does:The function converts a list of non-negative integers representing digits in a given base (between 2 and 40) to its equivalent decimal value. It accepts a list of digits and an integer base as input and returns the decimal value. The function handles empty lists by returning 0, ensuring consistency across all possible inputs. It does not modify the input list or perform any error checking on the base or digits beyond what is implicit in its calculation, implying it assumes the input is valid according to the specified constraints. The function's output is determined solely by the input digits and base, with no side effects or modifications to external state.

