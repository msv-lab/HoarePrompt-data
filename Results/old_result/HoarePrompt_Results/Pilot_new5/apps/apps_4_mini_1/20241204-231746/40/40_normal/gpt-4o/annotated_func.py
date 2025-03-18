#State of the program right berfore the function call: s is a non-empty string with a length of at most 50 characters, containing only lowercase English letters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome (reads the same forwards and backwards), and False otherwise.
#Overall this is what the function does:The function accepts a non-empty string `s` with a maximum length of 50 characters and returns `True` if `s` is a palindrome (reads the same forwards and backwards) and `False` otherwise. It does not handle any special cases for empty strings since `s` is guaranteed to be non-empty based on the input constraints.

