#State of the program right berfore the function call: s is a string, and char is a single character.
def func_1(s, char):
    first_occurrence = s.find(char)
    last_occurrence = s.rfind(char)
    if (first_occurrence != -1 and last_occurrence != -1) :
        if (first_occurrence == last_occurrence) :
            return s.replace(char, '', 1)
            #The program returns the string `s` with the first occurrence of the character `char` removed, as `char` appears only once in `s`.
        else :
            return s[:first_occurrence] + s[first_occurrence + 1:last_occurrence] + s[
    last_occurrence + 1:]
            #The program returns the string 's' with the first occurrence of 'char' removed, as well as the last occurrence of 'char', while keeping the rest of the string intact.
    else :
        return s
        #The program returns the string 's' regardless of the presence of 'char' in it
#Overall this is what the function does:The function accepts a string `s` and a single character `char`. It returns a modified version of `s`: if `char` appears only once in `s`, the function removes that single occurrence; if `char` appears more than once, it removes both the first and last occurrences of `char`; if `char` is not present in `s`, the function returns `s` unchanged. This functionality correctly handles cases when `char` appears multiple times, only once, or not at all.

