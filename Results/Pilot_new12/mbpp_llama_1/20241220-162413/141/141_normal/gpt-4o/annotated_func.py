#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    digit_str = str(n)
    frequency = {}
    for digit in digit_str:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is the string representation of `n`, if `digit_str` is not empty, then `frequency` is a dictionary where each key is a unique digit from `digit_str` and each value is the count of that digit in `digit_str`; otherwise, `frequency` is an empty dictionary.
    for (digit, count) in frequency.items():
        if count > int(digit):
            return False
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is the string representation of the original value of `n`, `frequency` is a dictionary where each key is a unique digit from `digit_str` and each value is the count of that digit in `digit_str`, and for each key-value pair in `frequency`, the value (count) is less than or equal to the integer value of the key (digit), or the function has returned False.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` as input, converts it into a string representation, counts the frequency of each digit in the string, and returns a boolean value indicating whether all digit counts are less than or equal to their respective digit values. If any digit count exceeds its digit value, the function immediately returns `False`. Otherwise, it returns `True` after checking all digits. The function handles edge cases such as an empty string representation (i.e., when `n` is 0), in which case `frequency` will be an empty dictionary and the function will return `True`. The function does not modify the input `n` and does not perform any actions other than the described digit frequency checks.

