#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    digit_str = str(n)
    frequency = {}
    for digit in digit_str:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is the string representation of `n`, `frequency` is a dictionary where the keys are the unique digits in `digit_str` and the values are the counts of those digits in `digit_str`.
    for (digit, count) in frequency.items():
        if count > int(digit):
            return False
        
    #State of the program after the  for loop has been executed: `frequency` is a dictionary where the keys are the unique digits in `digit_str` and the values are the counts of those digits in `digit_str`, and the function returns True if for every key-value pair (digit, count) in `frequency`, the count is less than or equal to the integer value of `digit`. Otherwise, the function returns False.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n`, converts it to a string to extract its digits, and then checks if the count of each digit is less than or equal to the numeric value of that digit. If for any digit the count exceeds its numeric value, the function returns `False`. Otherwise, it returns `True`. Potential edge cases include when `n` is 0 (which has no digits), and when `n` consists of a single digit repeated multiple times (e.g., 111). In such cases, the function still adheres to the rule that the count should not exceed the digit's value.

