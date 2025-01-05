#State of the program right berfore the function call: ch is a non-empty string consisting of lowercase English letters, with a length between 1 and 3000.
def func_1(ch):
    return not ch in 'aeiou'
    #The program returns True if 'ch' is a consonant (not in 'aeiou') and False if 'ch' is a vowel (is in 'aeiou')
#Overall this is what the function does:The function accepts a non-empty string `ch` consisting of lowercase English letters and returns True if `ch` is a consonant (not a vowel), and False if `ch` is a vowel. It does not handle cases for strings of length greater than one or any characters that are not lowercase English letters, which may lead to unexpected behavior if those cases are encountered.

