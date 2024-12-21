#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    digit_str = str(n)
    frequency = {}
    for digit in digit_str:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is a string containing all the digits of `n`, and `frequency` is a dictionary where each key is a digit from `digit_str` and its corresponding value is the frequency of that digit in `digit_str`.
    for (digit, count) in frequency.items():
        if count > int(digit):
            return False
        
    #State of the program after the  for loop has been executed: `frequency` is a dictionary with all key-value pairs where each count is less than or equal to the corresponding digit in `digit_str`, `n` is a non-negative integer, `digit_str` is a string containing all the digits of `n`.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and converts it into a string `digit_str` containing all its digits. It then creates a frequency dictionary `frequency` to store the count of each digit. After counting the digits, it checks if the count of any digit is greater than the digit itself. If such a case is found, the function returns `False`. Otherwise, it returns `True`. Potential edge cases include when `n` is 0 (which would still result in an empty string `digit_str`), and when `n` is a single-digit number (where `frequency` would contain only one entry).

