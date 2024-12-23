#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    digit_str = str(n)
    frequency = {}
    for digit in digit_str:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is the string representation of `n`, `frequency` is a dictionary where each key is a unique digit from `digit_str` and its corresponding value is the frequency of that digit in `digit_str`.
    for (digit, count) in frequency.items():
        if count > int(digit):
            return False
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is the string representation of `n`, `frequency` is a dictionary where each key is a unique digit from `digit_str` and its corresponding value is the frequency of that digit in `digit_str`. If for all digits in `digit_str`, the frequency of the digit is less than or equal to the integer value of the digit, then the loop completes without returning False. Otherwise, the function returns False as soon as it encounters a digit whose frequency exceeds its integer value.
    return True
    #The program returns True, indicating that the frequency of each digit in the string representation of `n` does not exceed the integer value of the digit.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns a boolean value indicating whether the frequency of each digit in the string representation of `n` does not exceed the integer value of the digit. The function iterates through each digit in the string representation of `n`, counts the frequency of each unique digit, and checks if this frequency is less than or equal to the integer value of the digit. If any digit's frequency exceeds its integer value, the function immediately returns `False`. Otherwise, it returns `True` after checking all digits. The function handles all non-negative integers, including single-digit numbers and numbers with repeated digits, and it correctly handles edge cases such as when `n` is 0 or when `n` contains multiple occurrences of the same digit. The function's return value provides a clear indication of whether the input number satisfies the specified condition.

