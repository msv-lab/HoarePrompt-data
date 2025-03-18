#State of the program right berfore the function call: s is a non-empty string with a maximum length of 50 characters, containing only lowercase English letters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome (reads the same backward as forward), otherwise returns False
#Overall this is what the function does:The function accepts a string `s` and returns `True` if `s` is a palindrome, otherwise returns `False`.

