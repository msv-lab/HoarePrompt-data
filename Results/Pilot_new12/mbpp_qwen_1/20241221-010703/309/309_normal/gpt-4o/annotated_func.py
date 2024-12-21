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
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string, all characters in `s` are equal to `first_char`.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts a non-empty string `s` and returns `True` if all characters in the string are the same, and `False` otherwise. The function checks the first character of the string and then iterates through the entire string to verify that every character matches the first one. If at least one character differs, it returns `False`. The function ensures that the input string is non-empty, as it immediately returns `True` if the string is empty (which would violate the requirement).

