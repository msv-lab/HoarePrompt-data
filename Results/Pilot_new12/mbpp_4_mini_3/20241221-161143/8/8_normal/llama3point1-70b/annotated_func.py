#State of the program right berfore the function call: s is a string, and char is a single character.
def func_1(s, char):
    first_occurrence = s.find(char)
    last_occurrence = s.rfind(char)
    if (first_occurrence != -1 and last_occurrence != -1) :
        if (first_occurrence == last_occurrence) :
            return s.replace(char, '', 1)
            #The program returns the string 's' with the single occurrence of 'char' replaced by an empty string, resulting in `s` without `char`.
        else :
            return s[:first_occurrence] + s[first_occurrence + 1:last_occurrence] + s[
    last_occurrence + 1:]
            #The program returns the string `s` with the first occurrence of `char` and the last occurrence of `char` removed, where `first_occurrence` is the index of the first occurrence of `char`, and `last_occurrence` is the index of the last occurrence of `char`.
    else :
        return s
        #The program returns the string `s`, which may or may not contain the character `char`, and where `first_occurrence` and `last_occurrence` are -1, indicating that `char` is not present in `s`.
#Overall this is what the function does:The function accepts a string `s` and a single character `char`. It performs the following actions based on the occurrences of `char` in `s`: 

1. If `char` appears exactly once in `s`, it returns the string `s` with that single occurrence of `char` removed.
2. If `char` appears two or more times in `s`, it returns the string `s` with both the first and the last occurrences of `char` removed.
3. If `char` is not present in `s`, it returns the original string `s` unchanged.

The function effectively modifies the input string `s` based on the count of the specified character `char`, handling cases where `char` may be absent or present multiple times.

