#State of the program right berfore the function call: ch is a non-empty string consisting of small English letters with a length between 1 and 3000 letters.**
def func_1(ch):
    return not ch in 'aeiou'
    #The program returns True if the string 'ch' does not contain any vowel (a, e, i, o, u), otherwise it returns False.
#Overall this is what the function does:The function func_1 accepts a non-empty string 'ch' and returns True if the string does not contain any vowels (a, e, i, o, u). Otherwise, it returns False. The code directly checks if the input string contains any vowels and returns the opposite result. It does not handle cases where the input is not a valid string or contains uppercase letters.

