#State of the program right berfore the function call: s is a string, and char is a single character.
def func_1(s, char):
    first_occurrence = s.find(char)
    last_occurrence = s.rfind(char)
    if (first_occurrence != -1 and last_occurrence != -1) :
        if (first_occurrence == last_occurrence) :
            return s.replace(char, '', 1)
            #The program returns the string 's' with the first occurrence of the character 'char' removed, indicating that 'char' appears only once in 's'.
        else :
            return s[:first_occurrence] + s[first_occurrence + 1:last_occurrence] + s[
    last_occurrence + 1:]
            #The program returns the string 's' with all occurrences of 'char' removed, where 'first_occurrence' is the index of the first occurrence and 'last_occurrence' is the index of the last occurrence, indicating that 'char' was found multiple times in 's'.
    else :
        return s
        #The program returns the string `s`, regardless of the presence of `char` in it.
#Overall this is what the function does:The function accepts a string `s` and a single character `char`. It returns the string `s` with the first occurrence of `char` removed if it appears once, or with all occurrences of `char` removed if it appears multiple times. If `char` is not present, it returns the string `s` unchanged. The function correctly identifies and handles cases where `char` does not exist in `s`, appears once, or appears multiple times.

