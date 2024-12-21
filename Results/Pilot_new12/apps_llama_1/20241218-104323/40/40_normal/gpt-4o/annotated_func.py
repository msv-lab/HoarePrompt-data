#State of the program right berfore the function call: s is a non-empty string containing at most 50 lowercase English letters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if string 's' is a palindrome and False otherwise, where 's' is a non-empty string containing at most 50 lowercase English letters.
#Overall this is what the function does:The function determines whether a given non-empty string of at most 50 lowercase English letters is a palindrome, returning True if the string reads the same backward as forward and False otherwise, without modifying the original string.

