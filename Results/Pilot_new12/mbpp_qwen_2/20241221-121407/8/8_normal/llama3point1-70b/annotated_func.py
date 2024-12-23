#State of the program right berfore the function call: s is a string and char is a single character string.
def func_1(s, char):
    first_occurrence = s.find(char)
    last_occurrence = s.rfind(char)
    if (first_occurrence != -1 and last_occurrence != -1) :
        if (first_occurrence == last_occurrence) :
            return s.replace(char, '', 1)
            #The program returns the string 's' with the first occurrence of 'char' removed
        else :
            return s[:first_occurrence] + s[first_occurrence + 1:last_occurrence] + s[
    last_occurrence + 1:]
            #The program returns the string 's' with the character 'char' removed from its first and last occurrence
    else :
        return s
        #The program returns string 's'
#Overall this is what the function does:The function `func_1` accepts two parameters: `s`, which is a string, and `char`, which is a single character string. It returns the string `s` modified based on the occurrences of `char` within `s`.

- If `char` appears exactly once in `s`, the function returns `s` with the first (and only) occurrence of `char` removed.
- If `char` appears more than once in `s`, the function returns `s` with the first and last occurrences of `char` removed.
- If `char` does not appear in `s` at all, the function returns the original string `s`.

Thus, the function modifies the string `s` according to the specified conditions, ensuring that the first and/or last occurrence of `char` is removed where applicable, or returns the original string if no such occurrences exist.

