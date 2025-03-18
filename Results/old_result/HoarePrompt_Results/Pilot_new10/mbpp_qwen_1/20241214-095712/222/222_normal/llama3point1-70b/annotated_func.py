#State of the program right berfore the function call: s is a string.
def func_1(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char
        
    #State of the program after the  for loop has been executed: `s` is a string, `result` is a concatenation of all uppercase characters from the string `s`.
    return result
    #The program returns the concatenation of all uppercase characters from string 's'
#Overall this is what the function does:The function `func_1` accepts a string `s` and returns a new string containing all the uppercase characters from `s`. This is achieved by iterating through each character in `s`, checking if it is uppercase using `char.isupper()`, and appending it to the `result` string if it is. The function handles all characters in the input string, including edge cases where the string is empty or contains no uppercase characters.

