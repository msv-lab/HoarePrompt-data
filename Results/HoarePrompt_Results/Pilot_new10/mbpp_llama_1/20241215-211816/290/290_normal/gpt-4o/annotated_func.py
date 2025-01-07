#State of the program right berfore the function call: s is a string.
def func_1(s):
    if ('z' in s[1:-1]) :
        return True
        #The program returns a boolean value True
    #State of the program after the if block has been executed: s is a string, and 'z' is not in the substring of s excluding the first and last characters
    return False
    #The program returns False
#Overall this is what the function does:The function accepts a string `s` and returns `True` if 'z' is found in the substring of `s` excluding the first and last characters, and `False` otherwise, including for empty strings or strings with less than 3 characters.

