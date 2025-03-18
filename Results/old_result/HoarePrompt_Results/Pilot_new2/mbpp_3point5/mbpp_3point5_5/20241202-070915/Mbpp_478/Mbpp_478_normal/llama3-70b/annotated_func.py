#State of the program right berfore the function call: **Precondition**: **s is a string.**
def func_1(s):
    return ''.join(c for c in s if c.isupper())
    #The program returns a new string that contains only the uppercase letters from the original string 's'.
#Overall this is what the function does:The function func_1 accepts a string parameter s and returns a new string that consists of only the uppercase letters present in the original string s.

