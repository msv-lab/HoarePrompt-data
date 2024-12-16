#State of the program right berfore the function call: s is a string and char is a single character that is present at least twice in s.
def func_1(s, char):
    first_occurrence = s.find(char)
    last_occurrence = s.rfind(char)
    if (first_occurrence != -1 and last_occurrence != -1) :
        if (first_occurrence == last_occurrence) :
            return s.replace(char, '', 1)
            #The program returns a string where the single occurrence of `char` has been removed from `s`.
        else :
            return s[:first_occurrence] + s[first_occurrence + 1:last_occurrence] + s[
    last_occurrence + 1:]
            #The program returns a string derived from `s` with the first and last occurrences of `char` removed, where `s` is the original string, and `char` is a character that appears at least twice in `s`.
    else :
        return s
        #The program returns string 's' which contains character 'char' with 'first_occurrence' and 'last_occurrence' being either valid indices of 'char' in 's' or -1 if 'char' is not present in 's' or not present at least twice
#Overall this is what the function does:The function accepts a string `s` and a character `char`, and returns a new string where the first and last occurrences of `char` are removed if `char` appears more than once in `s`, or the original string `s` if `char` appears once or not at all in `s`.

