#State of the program right berfore the function call: s is a non-empty string.
def func_1(s):
    if (not s) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: s is a non-empty string
    first_char = s[0]
    for char in s:
        if char != first_char:
            return False
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string, `first_char` is the first character of `s`. If every character in `s` is equal to `first_char`, the function returns True; otherwise, it returns False.
    return True
    #The program returns True
#Overall this is what the function does:The function accepts a non-empty string `s` and returns `True` if all characters in `s` are the same, otherwise it returns `False`.

