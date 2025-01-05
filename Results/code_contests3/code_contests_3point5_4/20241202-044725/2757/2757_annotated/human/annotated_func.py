#State of the program right berfore the function call: ch is a non-empty string consisting of small English letters. The length of ch is between 1 and 3000.**
def func_1(ch):
    return not ch in 'aeiou'
    #The program returns True if the non-empty string 'ch' does not contain any vowels ('a', 'e', 'i', 'o', 'u'), otherwise it returns False.
#Overall this is what the function does:The function func_1 accepts a non-empty string ch and returns True if the string does not contain any vowels (a, e, i, o, u). Otherwise, it returns False. The code directly checks if any vowels are present in the string and returns the opposite result, which is not in line with the annotations stating that it should return True when no vowels are present.

