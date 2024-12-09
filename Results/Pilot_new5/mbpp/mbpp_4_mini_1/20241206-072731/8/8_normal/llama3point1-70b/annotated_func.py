#State of the program right berfore the function call: s is a string, and char is a single character.
def func_1(s, char):
    first_occurrence = s.find(char)
    last_occurrence = s.rfind(char)
    if (first_occurrence != -1 and last_occurrence != -1) :
        if (first_occurrence == last_occurrence) :
            return s.replace(char, '', 1)
            #The program returns the string 's' with the single occurrence of 'char' removed, resulting in a modified string where 'char' appears exactly once in 's'.
        else :
            return s[:first_occurrence] + s[first_occurrence + 1:last_occurrence] + s[
    last_occurrence + 1:]
            #The program returns the string 's' with the first and last occurrences of 'char' removed, resulting in a new string formed by concatenating the segments of 's' before the first occurrence, between the first and last occurrences, and after the last occurrence.
    else :
        return s
        #The program returns the string 's' which has not been affected by the occurrences of 'char' since first_occurrence and last_occurrence indicate that 'char' is not found in 's'.
#Overall this is what the function does:The function accepts a string `s` and a single character `char`. It removes one occurrence of `char` if it appears exactly once in `s`, removes both the first and last occurrences of `char` if it appears more than once, and returns the original string `s` if `char` is not found. This function does not handle cases where the string may contain more than two occurrences of `char` and, therefore, does not account for any additional removals beyond the specified conditions.

