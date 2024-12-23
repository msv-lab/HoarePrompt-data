#State of the program right berfore the function call: s is a string and char is a single character that exists at least twice in s.
def func_1(s, char):
    first_occurrence = s.find(char)
    last_occurrence = s.rfind(char)
    if (first_occurrence != -1 and last_occurrence != -1) :
        if (first_occurrence == last_occurrence) :
            return s.replace(char, '', 1)
            #The program returns a string where the first occurrence of `char` has been removed, resulting in a modified version of `s`.
        else :
            return s[:first_occurrence] + s[first_occurrence + 1:last_occurrence] + s[
    last_occurrence + 1:]
            #The program returns a string that is derived from `s` with the first and last occurrences of `char` removed, where `s` is the original string, `char` is a character that exists at least twice in `s`, `first_occurrence` is the index of the first occurrence of `char` in `s`, and `last_occurrence` is the index of the last occurrence of `char` in `s`.
    else :
        return s
        #The program returns string `s` that contains at least one character `char` which appears at least twice, with `first_occurrence` and `last_occurrence` indices associated with `char` in `s`, where either or both of these indices can be -1
#Overall this is what the function does:The function `func_1` accepts a string `s` and a character `char` as input, and returns a modified string based on the occurrence of `char` in `s`. If `char` appears more than once in `s`, it removes the first and last occurrences of `char` from `s` and returns the resulting string. If `char` appears only once in `s`, it removes the single occurrence of `char` from `s` and returns the resulting string. If `char` does not appear in `s`, it returns the original string `s`. The function handles edge cases where `char` is not found in `s` or appears only once, and it correctly handles the case where `char` appears multiple times in `s`. After executing the function, the resulting string will have the first and last occurrences of `char` removed if `char` appears more than once, or the single occurrence of `char` removed if `char` appears only once, or will be the original string `s` if `char` is not found in `s`.

