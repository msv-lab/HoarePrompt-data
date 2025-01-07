#State of the program right berfore the function call: s is a string.
def func_1(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char
        
    #State of the program after the  for loop has been executed: `s` is the original string, `result` is a string containing all the uppercase characters from `s`, `char` is the last character in `s`.
    return result
    #The program returns a string containing all the uppercase characters from the original string `s`.
#Overall this is what the function does:The function accepts a string and returns a new string containing all the uppercase characters from the original string. It correctly handles empty strings and strings with only lowercase characters, returning an empty string in these cases. However, it may throw an error if the input is not a string.

