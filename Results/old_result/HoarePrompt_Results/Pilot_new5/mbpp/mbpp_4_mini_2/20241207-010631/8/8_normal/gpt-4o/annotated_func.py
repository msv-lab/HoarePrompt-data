#State of the program right berfore the function call: s is a string and ch is a single character string.
def func_1(s, ch):
    first_index = s.find(ch)
    last_index = s.rfind(ch)
    if (first_index == -1 or last_index == -1 or first_index == last_index) :
        return s
        #The program returns the string 's', which may indicate that the character 'ch' is not found in the string or that its first and last occurrences are the same, given the current values of first_index and last_index.
    #State of the program after the if block has been executed: *`s` is a string, `ch` is a single character string, `first_index` is the index of the first occurrence of `ch` in `s` (which is not -1), `last_index` is the index of the last occurrence of `ch` in `s` (which is not -1), and `first_index` is not equal to `last_index`.
    return s[:first_index] + s[first_index + 1:last_index] + s[last_index + 1:]
    #The program returns the string `s` with the first occurrence of `ch` removed and the last occurrence of `ch` removed, while preserving the characters in between.
#Overall this is what the function does:The function accepts a string `s` and a single character string `ch`. It returns the original string `s` if `ch` is not found or if the first and last occurrences of `ch` in `s` are the same. If `ch` occurs multiple times in `s`, it returns `s` with the first and last occurrences of `ch` removed while preserving the characters in between.

