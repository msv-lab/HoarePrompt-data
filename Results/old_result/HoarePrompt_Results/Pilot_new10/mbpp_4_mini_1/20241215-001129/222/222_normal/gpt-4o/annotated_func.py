#State of the program right berfore the function call: s is a string that may contain lowercase substrings to be removed.
def func_1(s):
    return ''.join([char for char in s if char.isupper()])
    #The program returns a string that contains only the uppercase characters from the original string 's'
#Overall this is what the function does:The function accepts a string `s` and returns a new string that contains only the uppercase characters from `s`. If `s` does not contain any uppercase characters, the function returns an empty string.

