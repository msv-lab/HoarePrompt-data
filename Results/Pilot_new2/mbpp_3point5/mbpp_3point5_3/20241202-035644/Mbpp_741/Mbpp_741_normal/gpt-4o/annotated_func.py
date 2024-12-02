#State of the program right berfore the function call: s is a string containing characters.
def func_1(s):
    if (not s) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: *s is a string containing characters and it is not empty
    first_char = s[0]
    for char in s:
        if char != first_char:
            return False
        
    #State of the program after the  for loop has been executed: The loop will return False if there is a character in the string `s` that is different from the first character `first_char`. Otherwise, the loop will continue until the end of the string. In the end, `s` is a non-empty string containing characters, and all characters are equal to `first_char`, `first_char` remains the same.
    return True
    #The program returns True if all characters in string `s` are equal to the first character `first_char`, otherwise it returns False
#Overall this is what the function does:The function func_1 accepts a string parameter s. It returns True if the string is empty and False if any character in the string differs from the first character. If all characters in the string are equal to the first character, it returns True.

