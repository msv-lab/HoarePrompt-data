#State of the program right berfore the function call: s is a string and c is a character.**
def func_1(s, c):
    first_occ = s.find(c)
    last_occ = s.rfind(c)
    if (first_occ != -1 and last_occ != -1) :
        return s[:first_occ] + s[first_occ + 1:last_occ] + s[last_occ + 1:]
        #The program returns the string s with the character at the index of first_occ and last_occ removed
    else :
        return s
        #The program returns the string s
#Overall this is what the function does:The function `func_1` accepts a string `s` and a character `c`. It then removes the characters at the indices of the first and last occurrences of character `c` in the string `s` and returns the modified string. If the character `c` is not found in the string `s`, the function simply returns the original string `s`.

