#State of the program right berfore the function call: s is a string and c is a character.**
def func_1(s, c):
    first_occ = s.find(c)
    last_occ = s.rfind(c)
    if (first_occ != -1 and last_occ != -1) :
        return s[:first_occ] + s[first_occ + 1:last_occ] + s[last_occ + 1:]
        #The program returns the string 's' with the character at index first_occ removed along with the characters between first_occ and last_occ, and the character at index last_occ removed
    else :
        return s
        #The program returns the string s
#Overall this is what the function does:The function `func_1` accepts a string `s` and a character `c`. If both the first and last occurrences of the character `c` are found in the string `s`, it returns `s` with the character at index `first_occ` removed, along with the characters between `first_occ` and `last_occ`, and the character at index `last_occ` removed. If either the first or last occurrence of the character `c` is not found, the function returns the original string `s`.

