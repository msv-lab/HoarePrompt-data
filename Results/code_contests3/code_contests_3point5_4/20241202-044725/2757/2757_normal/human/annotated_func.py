#State of the program right berfore the function call: ch is a non-empty string consisting of small English letters. The length of the string is between 1 and 3000 letters.**
def func_1(ch):
    return not ch in 'aeiou'
    #The program returns True if the character in the string 'ch' is not a vowel (a, e, i, o, u), otherwise it returns False.
#Overall this is what the function does:The function func_1 accepts a non-empty string ch consisting of small English letters. It returns True if the character in the string ch is not a vowel (a, e, i, o, u); otherwise, it returns False.

