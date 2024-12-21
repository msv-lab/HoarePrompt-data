#State of the program right berfore the function call: s is a string and char is a single character.
def func_1(s, char):
    first_occurrence = s.find(char)
    last_occurrence = s.rfind(char)
    if (first_occurrence != -1 and last_occurrence != -1) :
        if (first_occurrence == last_occurrence) :
            return s.replace(char, '', 1)
            #The program returns the string 's' with the character 'char' removed once, indicating that 'char' occurs exactly once in 's'.
        else :
            return s[:first_occurrence] + s[first_occurrence + 1:last_occurrence] + s[
    last_occurrence + 1:]
            #The program returns the substring of 's' that excludes the first and last occurrence of 'char'
    else :
        return s
        #The program returns the string 's'
#Overall this is what the function does:The function accepts a string `s` and a single character `char`, and modifies the string based on the occurrences of `char`. If `char` occurs exactly once in `s`, it removes `char` from `s` once. If `char` occurs multiple times, it returns the substring of `s` that excludes both the first and last occurrences of `char`. If `char` does not occur in `s` at all, the function returns the original string `s`. The function is designed to handle cases where `char` is either absent, present once, or present multiple times. However, it does not account for cases where `char` might be an empty string or if the string `s` is empty. In such cases, it will return the string `s` unaffected.

