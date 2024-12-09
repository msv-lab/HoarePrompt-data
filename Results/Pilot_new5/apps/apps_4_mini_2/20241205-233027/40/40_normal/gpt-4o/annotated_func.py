#State of the program right berfore the function call: s is a non-empty string containing at most 50 lowercase English letters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome (reads the same forwards and backwards), otherwise it returns False.
#Overall this is what the function does:The function accepts a non-empty string `s` and returns `True` if `s` is a palindrome and `False` otherwise.

