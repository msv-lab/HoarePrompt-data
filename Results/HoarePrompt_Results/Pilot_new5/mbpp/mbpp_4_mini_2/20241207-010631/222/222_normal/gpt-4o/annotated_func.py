#State of the program right berfore the function call: s is a string that may contain lowercase substrings.
def func_1(s):
    return ''.join([char for char in s if char.isupper()])
    #The program returns an empty string because the initial string 's' may contain only lowercase substrings, and no uppercase characters are present to join.
#Overall this is what the function does:The function accepts a string `s` and returns a new string containing only the uppercase characters from `s`. If `s` contains no uppercase characters, it returns an empty string.

