#State of the program right berfore the function call: s is a string and c is a character.
def func_1(s, c):
    first_occ = s.find(c)
    last_occ = s.rfind(c)
    if (first_occ != -1 and last_occ != -1) :
        return s[:first_occ] + s[first_occ + 1:last_occ] + s[last_occ + 1:]
        #The program returns string s with the character at index first_occ removed, as well as the character at index last_occ removed
    else :
        return s
        #The program returns string s
#Overall this is what the function does:The function `func_1` accepts a string `s` and a character `c`. If the character `c` is found at multiple positions within the string `s`, the function removes the first and last occurrences of `c` from the string `s` and returns the modified string. If the character `c` is not found within the string `s`, the function simply returns the original string `s`.

