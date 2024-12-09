#State of the program right berfore the function call: s is a string that may contain lowercase substrings.
def func_1(s):
    return ''.join([char for char in s if char.isupper()])
    #The program returns a string that contains only the uppercase characters from the string 's'
#Overall this is what the function does:The function accepts a string `s` and returns a new string containing only the uppercase characters from `s`. If there are no uppercase characters in `s`, the function will return an empty string.

