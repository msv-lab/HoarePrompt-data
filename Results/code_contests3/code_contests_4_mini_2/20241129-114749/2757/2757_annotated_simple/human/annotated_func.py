#State of the program right berfore the function call: ch is a non-empty string consisting of small English letters with a length between 1 and 3000.
def func_1(ch):
    return not ch in 'aeiou'
    #The program returns True if 'ch' is not a vowel (not in 'aeiou') and False if 'ch' is a vowel.
#Overall this is what the function does:The function accepts a non-empty string `ch` consisting of lowercase English letters and returns True if `ch` is not a vowel (i.e., it is one of the consonants), and False if `ch` is a vowel ('a', 'e', 'i', 'o', 'u').

