#State of the program right berfore the function call: s is a string and char is a single character string.
def func_1(s, char):
    first_occurrence = s.find(char)
    last_occurrence = s.rfind(char)
    if (first_occurrence != -1 and last_occurrence != -1) :
        if (first_occurrence == last_occurrence) :
            return s.replace(char, '', 1)
            #The program returns the string 's' with the first occurrence of 'char' replaced by an empty string
        else :
            return s[:first_occurrence] + s[first_occurrence + 1:last_occurrence] + s[
    last_occurrence + 1:]
            #The program returns a string from `s` with the character `char` removed at both `first_occurrence` and `last_occurrence` indices
    else :
        return s
        #The program returns string 's'
#Overall this is what the function does:The function `func_1` accepts a string `s` and a single character string `char`. If `char` appears only once in `s`, it returns `s` with the first occurrence of `char` removed. If `char` appears more than once in `s`, it returns `s` with the characters at both the first and last occurrences of `char` removed. If `char` does not appear in `s`, it returns `s` unchanged.

