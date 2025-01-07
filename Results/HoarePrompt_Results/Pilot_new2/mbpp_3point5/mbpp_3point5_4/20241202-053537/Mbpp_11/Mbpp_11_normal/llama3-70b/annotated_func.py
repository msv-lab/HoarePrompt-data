#State of the program right berfore the function call: s is a string, and c is a character.**
def func_1(s, c):
    first_occ = s.find(c)
    last_occ = s.rfind(c)
    if (first_occ != -1 and last_occ != -1) :
        return s[:first_occ] + s[first_occ + 1:last_occ] + s[last_occ + 1:]
        #The program returns the string `s` with the characters between the first occurrence and the last occurrence of character `c` removed.
    else :
        return s
        #The program returns the string `s`
#Overall this is what the function does:The function func_1 accepts two parameters: a string `s` and a character `c`. It returns the string `s` with characters between the first and last occurrences of `c` removed if `c` is found. If `c` is not found, it returns the original string `s`.

