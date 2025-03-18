#State of the program right berfore the function call: **Precondition**: **s is a string.**
def func_1(s):
    return ''.join(c for c in s if c.isupper())
    #The program returns a string containing all the uppercase characters present in the string 's'.
#Overall this is what the function does:The function func_1 accepts a string `s` as a parameter and returns a new string containing only the uppercase characters found in the input string `s`. It filters out any non-uppercase characters from the input string `s` and returns the result.

