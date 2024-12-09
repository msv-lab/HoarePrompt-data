#State of the program right berfore the function call: s is a non-empty string of length at most 50, containing only lowercase English letters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome, meaning it reads the same forwards and backwards; otherwise, it returns False.
#Overall this is what the function does:The function accepts a non-empty string `s` containing only lowercase English letters and returns True if `s` is a palindrome (reads the same forwards and backwards); otherwise, it returns False.

