#State of the program right berfore the function call: s is a string and char is a single character.
def func_1(s, char):
    first_occurrence = s.find(char)
    last_occurrence = s.rfind(char)
    if (first_occurrence != -1 and last_occurrence != -1) :
        if (first_occurrence == last_occurrence) :
            return s.replace(char, '', 1)
            #The program returns the string 's' with the single occurrence of 'char' removed, resulting in a string where 'char' appears exactly once in 's'
        else :
            return s[:first_occurrence] + s[first_occurrence + 1:last_occurrence] + s[
    last_occurrence + 1:]
            #The program returns a new string formed by removing the character at `first_occurrence` and the character at `last_occurrence` from the string `s`, while keeping the rest of the string intact. The indices `first_occurrence` and `last_occurrence` are different, ensuring that two characters are removed.
    else :
        return s
        #The program returns the string 's'
#Overall this is what the function does:The function accepts a string `s` and a character `char`. It returns a new string based on the occurrences of `char`: if `char` appears exactly once in `s`, it removes that occurrence; if `char` appears multiple times, it removes both the first and the last occurrences; if `char` does not exist in `s`, it returns the original string unchanged.

