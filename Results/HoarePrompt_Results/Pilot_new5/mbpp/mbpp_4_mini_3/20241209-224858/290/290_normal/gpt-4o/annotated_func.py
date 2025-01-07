#State of the program right berfore the function call: s is a string of characters where the first and last characters can be any character except 'z', and the string can be of any length.
def func_1(s):
    if ('z' in s[1:-1]) :
        return True
        #The program returns True because the string 's' contains at least one 'z' in the substring from the second character to the second-to-last character.
    #State of the program after the if block has been executed: *`s` is a string of characters where the first and last characters can be any character except 'z', the string can be of any length, and there is no 'z' between the first and last characters of `s`.
    return False
    #The program returns False
#Overall this is what the function does:The function accepts a string `s` and checks for the presence of the character 'z' in the substring from the second character to the second-to-last character. It returns True if at least one 'z' is found within that substring; otherwise, it returns False. If the string has a length of 2 or less, the substring is empty, and the function will return False since there cannot be any 'z' in an empty substring.

